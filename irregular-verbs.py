#!/usr/bin/env python

"""
A trainer for English irregular verbs built with Qt.
"""

__author__ = "Tal Zana"
__copyright__ = "Copyright 2021"
__license__ = "GPL"
__version__ = "1.0"

import sys
import random

from PySide6.QtWidgets import (
    QApplication, QHBoxLayout, QLabel, QLineEdit,
    QMessageBox, QVBoxLayout, QWidget
)
from PySide6.QtGui import QKeyEvent
from PySide6.QtCore import Qt

from verbs import VERBS


CSS_LABEL = 'QLabel {font-size: 32px;}'
CSS_LINE_EDIT = 'QLineEdit {font-size: 32px;}'
LINE_EDIT_HEIGHT = 48
MAX_QUESTIONS = 10


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle('Irregular Verbs')

        self.max_questions = MAX_QUESTIONS
        self.current_question = 0
        self.score = 0
        self.verb = {}
        self.done_verbs = []
        self.is_paused = False

        # Labels for displaying the verb and the score
        self.lbl_verb = QLabel()
        self.lbl_verb.setStyleSheet(CSS_LABEL)
        self.lbl_score = QLabel()
        self.lbl_score.setStyleSheet(CSS_LABEL)
        self.lbl_score.setAlignment(Qt.AlignRight)

        # Two inputs fields for past and participle forms
        self.inputs = {
            'past': QLineEdit(),
            'part': QLineEdit()
        }
        for i in self.inputs.values():
            i.setFixedHeight(LINE_EDIT_HEIGHT)
            i.setStyleSheet(CSS_LINE_EDIT)

        # Layout
        vb_main = QVBoxLayout()

        hb_message = QHBoxLayout()
        hb_message.addWidget(self.lbl_verb)
        hb_message.addWidget(self.lbl_score)

        hb_input = QHBoxLayout()
        for i in self.inputs.values(): hb_input.addWidget(i)

        vb_main.addLayout(hb_message)
        vb_main.addLayout(hb_input)

        vb_main.addStretch()

        self.setLayout(vb_main)

        self.new_game()

    def new_game(self):
        '''Start a new round of questions.'''
        self.score = 0
        self.current_question = 0
        self.lbl_score.setText(str(self.score))
        self.new_verb()

    def new_verb(self):
        '''Select a random verb and wait for user input.'''
        current_verb = VERBS.pop(random.randrange(0, len(VERBS)))
        self.done_verbs.append(current_verb)
        (self.verb['present'], self.verb['past'], self.verb['part']) = current_verb
        self.lbl_verb.setText(self.verb['present'])
        self.clear_inputs()
        self.inputs['past'].setFocus()
        self.current_question += 1
        self.is_paused = False
    
    def check_input(self):
        '''Check if user has answered correctly.'''
        self.disable_inputs()
        self.is_paused = True

        # Iterate over the two input fields
        # Color the answers green or red and adjust the score
        for k in self.inputs.keys():
            if self.inputs[k].text() in self.verb[k]:
                self.inputs[k].setStyleSheet('color: green')
                self.inputs[k].setText(self.correct_answer(self.verb[k]))
                self.score += 1
            else:
                self.inputs[k].setStyleSheet('color: red')
                self.inputs[k].setText(self.correct_answer(self.verb[k]))

        self.lbl_score.setText(str(self.score))

    def disable_inputs(self):
        for i in self.inputs.values():
            i.setDisabled(True)
    
    def clear_inputs(self):
        for i in self.inputs.values():
            i.setEnabled(True)
            i.setStyleSheet('')
            i.clear()

    def correct_answer(self, options: tuple) -> str:
        '''Return aa suitable string accounting for verbs with two options.'''
        if len(options) == 1:
            return options[0]
        else:
            return f'{options[0]}/{options[1]}'

    def game_over(self):
        '''Display end of round dialog.'''
        mbox = QMessageBox(self)
        mbox.setText(f'Score : {self.score}/{self.max_questions * 2}')
        mbox.setInformativeText('Allez, une petite dernière ?\n')
        mbox.addButton('Quitter', QMessageBox.NoRole)
        new = mbox.addButton('Nouvelle partie', QMessageBox.YesRole)
        new.setDefault(True)

        if mbox.exec():
            self.new_game()
        else:
            self.close()

    def keyPressEvent(self, event: QKeyEvent) -> QKeyEvent:
        '''Handle the 3 uses of the Enter key.'''

        if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:

            # Use Enter to move from left to right input field
            if self.inputs['past'].hasFocus():
                self.inputs['part'].setFocus()

            # Also use Enter to advance to next verb
            if self.is_paused:
                if self.current_question < self.max_questions:
                    self.new_verb()
                else:
                    self.game_over()

            # Validate the answer if both fields contain text
            if self.inputs['past'].text() and self.inputs['part'].text():
                self.check_input()

        return super().keyPressEvent(event)


def main():
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
    sys.exit()


if __name__ == '__main__':
    main()
