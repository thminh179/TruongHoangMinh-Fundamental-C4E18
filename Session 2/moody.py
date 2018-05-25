# random a mood: 0-30~T.T / 30-60~.-. / 60-100~xD

from random import randint

numb = randint(0, 101)

if 0< numb <30: print("T.T")
elif 30< numb < 60: print(".-.")
else: print("xD")
