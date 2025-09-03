import matplotlib.pyplot as plt
import matplotlib as mpl

import numpy as np

code1 = "00"
ABC = {chr(65): code1}
for symb in range(66, 91):
    if symb != 74:
        code2 = int(code1, 5) + 1
        code1 = ""
        while code2 > 0:
            code1 = str(code2 % 5) + code1
            code2 //= 5
        ABC[chr(symb)] = code1
    else:
        code1 = "__"
        ABC[chr(symb)] = code1
        code1 = "13"
for i in ABC:
    while len(ABC[i]) < 2:
        ABC[i] = "0" + ABC[i]

word = input().upper()

listword = []
for i in word.upper():
    if i in ABC or i == " ":
        listword.append(i)
if not listword:
    print("error. available characters: latin".upper())

splitword = word.split()
maxlen = 0
for i in splitword:
    if maxlen < len(i):
        maxlen = len(i)

fig, ax = plt.subplots()
ax.set_aspect("equal", adjustable="datalim")
ax.set_box_aspect(len(splitword) / maxlen)
ax.autoscale()

ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

fig.patch.set_facecolor('black')

ax.patch.set_facecolor('black')

cmap = mpl.colormaps['autumn']
list_colors = cmap(np.linspace(0, 1, len(listword)))

x = 0
y = 0
RADIUS = 0.2

def settings_Circle(x1, y1, radius, color):
    ax.add_patch(plt.Circle((x1, y1), radius, color=color, fill=False, linewidth=3))

for ind, letter in enumerate(listword):
    x1 = x
    if letter == " ":
        x = 0
        y -= 0.4
    else:
        settings_Circle(x, y, RADIUS, list_colors[ind])
        symbols = ABC[letter]
        if symbols != "__":
            for c, i in enumerate(symbols):
                if i == "0":
                    RADIUS *= 2 / 3
                    settings_Circle(x, y, RADIUS, list_colors[ind])
                elif i == "1":
                    settings_Circle(x + RADIUS / 3, y, RADIUS * 2 / 3, list_colors[ind])
                    settings_Circle(x - RADIUS * 2 / 3, y, RADIUS / 3, list_colors[ind])
                    x += RADIUS / 3
                    RADIUS *= 2 / 3
                elif i == "2":
                    settings_Circle(x + RADIUS * 2 / 3, y, RADIUS / 3, list_colors[ind])
                    settings_Circle(x - RADIUS / 3, y, RADIUS * 2 / 3, list_colors[ind])
                    x -= RADIUS / 3
                    RADIUS *= 2 / 3
                elif i == "3":
                    settings_Circle(x + RADIUS * 2 / 3, y, RADIUS / 3, list_colors[ind])
                    settings_Circle(x, y, RADIUS / 3, list_colors[ind])
                    settings_Circle(x - RADIUS * 2 / 3, y, RADIUS / 3, list_colors[ind])
                    x -= RADIUS * 2 / 3
                    RADIUS /= 3
                elif i == "4":
                    settings_Circle(x + RADIUS / 2, y, RADIUS / 2, list_colors[ind])
                    settings_Circle(x - RADIUS / 2, y, RADIUS / 2, list_colors[ind])
                    x -= RADIUS / 2
                    RADIUS /= 2
        x = x1 + 0.4
        RADIUS = 0.2

plt.show()