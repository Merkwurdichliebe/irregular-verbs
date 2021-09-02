from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
build_options_app = {
    'iconfile': 'extras/Icon-MacOS-512x512@1x.icns',
    'bundle_name': 'Irregular Verbs'
    }

build_options_dmg = {
    'volume_label': 'Irregular Verbs'
}

import sys
base = 'Win32GUI' if sys.platform=='win32' else None

executables = [
    Executable(
        'verbes-gui.py',
        base = base, 
        target_name = 'Irregular Verbs')
]

setup(name='Irregular Verbs',
      version = '1.0',
      description = '',
      options = {
          'bdist_mac': build_options_app,
          'bdist_dmg': build_options_dmg
          },
      executables = executables)
