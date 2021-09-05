import json

from verbs import VERBS

verb_list = []

for item in VERBS:
    d = {'present': item[0]}
    if len(item[1]) > 1:
        d['preterit'] = item[1][0] + '/' + item[1][1]
    else:
        d['preterit'] = item[1][0]
    if len(item[2]) > 1:
        d['participle'] = item[2][0] + '/' + item[2][1]
    else:
        d['participle'] = item[2][0]
    verb_list.append(
        [
            d['present'],
            d['preterit'],
            d['participle']
        ]
    )

with open('verbs.json', 'w') as write_file:
  json.dump(verb_list,
            write_file,
            default=vars,
            indent=4,
            ensure_ascii=False,
           )