import json
import random

with open("data/op.json", "r",
          encoding='utf-8') as jsonfile:
    data = json.load(jsonfile)


def opBot():
    num = len(data['opBot'])

    key = random.randint(1, num)

    key = str(key)

    return data['opBot'][key]

print(opBot())