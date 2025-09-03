import matplotlib.pyplot as plt
import matplotlib as mpl

import numpy as np
from math import sqrt


code1 = "00"
ABC = {chr(1040): code1}
for symb in range(1041, 1072):
    code2 = int(code1, 8) + 1
    code1 = ""
    while code2 > 0:
        code1 = str(code2 % 8) + code1
        code2 //= 8
    ABC[chr(symb)] = code1

ABC['Ё'] = "__"

for i in ABC:
    while len(ABC[i]) < 2:
        ABC[i] = "0" + ABC[i]

word = input().upper()

for symbol in word:
    if not symbol in ABC.keys() and symbol != " ":
        print("ОШИБКА. ТЕКСТ ДОЛЖЕН СОДЕРЖАТЬ КИРИЛЛИЦУ")

listword = []
for i in word.upper():
    if i in ABC or i == " ":
        listword.append(i)

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
RADIUS = 1

def settings_Circle(x, y, radius, color):
    ax.add_patch(plt.Circle((x, y), radius, color=color, fill=False, linewidth=0.8))

def zero(RADIUS, x, y, color):
    settings_Circle(x, y, RADIUS* 2/3, color=color)

def one(RADIUS, x, y, color):
    settings_Circle(x + RADIUS / 3, y, RADIUS * 2 / 3, color=color)
    settings_Circle(x - RADIUS * 2 / 3, y, RADIUS / 3, color=color)

def two(RADIUS, x, y, color):
    settings_Circle(x + RADIUS * 2 / 3, y, RADIUS / 3, color=color)
    settings_Circle(x - RADIUS / 3, y, RADIUS * 2 / 3, color=color)

def three(RADIUS, x, y, color):
    settings_Circle(x + RADIUS * 2 / 3, y, RADIUS / 3, color=color)
    settings_Circle(x, y, RADIUS / 3, color=color)
    settings_Circle(x - RADIUS * 2 / 3, y, RADIUS / 3, color=color)

def four(RADIUS, x, y, color):
    settings_Circle(x + RADIUS / 2, y, RADIUS / 2, color=color)
    settings_Circle(x - RADIUS / 2, y, RADIUS / 2, color=color)

def five(RADIUS, x, y, color):
    y1 = y + (2 / (2 + sqrt(3))) * RADIUS
    ax.add_patch(plt.Circle((x, y1), (2 * sqrt(3) - 3) * RADIUS, color=color, fill=False, linewidth=0.8))
    ax.add_patch(plt.Circle((x + (2 / (2 + sqrt(3))) * RADIUS * sqrt(3) / 2, y - (2 / (2 + sqrt(3))) * RADIUS / 2),
                            (2 * sqrt(3) - 3) * RADIUS, color=color, fill=False, linewidth=0.8))
    ax.add_patch(plt.Circle((x - (2 / (2 + sqrt(3))) * RADIUS * sqrt(3) / 2, y - (2 / (2 + sqrt(3))) * RADIUS / 2),
                            (2 * sqrt(3) - 3) * RADIUS, color=color, fill=False, linewidth=0.8))

def six(RADIUS, x, y, color):
    y1 = y - (2 / (2 + sqrt(3))) * RADIUS
    ax.add_patch(plt.Circle((x, y1), (2 * sqrt(3) - 3) * RADIUS, color=color, fill=False, linewidth=0.8))
    ax.add_patch(plt.Circle((x + (2 / (2 + sqrt(3))) * RADIUS * sqrt(3) / 2, y + (2 / (2 + sqrt(3))) * RADIUS / 2),
                            (2 * sqrt(3) - 3) * RADIUS, color=color, fill=False, linewidth=0.8))
    ax.add_patch(plt.Circle((x - (2 / (2 + sqrt(3))) * RADIUS * sqrt(3) / 2, y + (2 / (2 + sqrt(3))) * RADIUS / 2),
                            (2 * sqrt(3) - 3) * RADIUS, color=color, fill=False, linewidth=0.8))

def seven():
    return 0

for ind, letter in enumerate(listword):
    x1 = x
    if letter == " ":
        x = 0
        y -= 2
    else:
        settings_Circle(x, y, RADIUS, list_colors[ind])
        symbols = ABC[letter]
        if symbols != "__":
            for c, i in enumerate(symbols):
                if i == "0":
                    zero(RADIUS, x, y, list_colors[ind])
                    RADIUS *= 2 / 3
                elif i == "1":
                    one(RADIUS, x, y, list_colors[ind])
                    x += RADIUS / 3
                    RADIUS *= 2 / 3
                elif i == "2":
                    two(RADIUS, x, y, list_colors[ind])
                    x -= RADIUS / 3
                    RADIUS *= 2 / 3
                elif i == "3":
                    three(RADIUS, x, y, list_colors[ind])
                    x -= RADIUS * 2 / 3
                    RADIUS /= 3
                elif i == "4":
                    four(RADIUS, x, y, list_colors[ind])
                    x -= RADIUS / 2
                    RADIUS /= 2
                elif i == '5':
                    five(RADIUS, x, y, list_colors[ind])
                elif i == '6':
                    six(RADIUS, x, y, list_colors[ind])
                elif i == '7':
                    seven()

        x = x1 + 2
        RADIUS = 1

plt.show()