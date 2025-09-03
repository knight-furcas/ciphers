import matplotlib.pyplot as plt
import matplotlib as mpl

import numpy as np

# ABC
code1 = "000"
ABC = {chr(65): code1}
for symb in range(66, 91):
    code2 = int(code1, 3) + 1
    code1 = ""
    while code2 > 0:
        code1 = str(code2 % 3) + code1
        code2 //= 3
    ABC[chr(symb)] = code1
for i in ABC:
    while len(ABC[i]) < 3:
        ABC[i] = "0" + ABC[i]

ABC[" "] = " "

# input
word = input().upper()

listword = []
for i in word.upper():
    if i in ABC:
        listword.append(i)

if not listword:
    print("error. available characters: latin".upper())

row = 0
line = 0

fig, ax = plt.subplots(layout='constrained')
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)
plt.gcf().set_size_inches(len(listword), 3 / (2 ** 0.5))
plt.grid(False)
plt.axis('off')

fig.patch.set_facecolor('black')

cmap = mpl.colormaps['autumn']
list_colors = cmap(np.linspace(0, 1, len(listword)))

for c, i in enumerate(listword):
    color = list_colors[c]
    if i == " ":
        row += 6
    else:
        for symbol in ABC[i]:
            if symbol == "0":
                x = np.linspace(row - 1, row + 1, 100)
                y = np.linspace(line - 1, line + 1, 100)
                ax.plot(x, y, linewidth=5.0, color=color)
            elif symbol == "что-то":
                x = np.linspace(row - 1, row + 1, 100)
                y = np.linspace(line + 1, line - 1, 100)
                ax.plot(x, y, linewidth=5.0, color=color)
            else:
                x = np.linspace(row - 1, row + 1, 100)
                y = np.linspace(line - 1, line + 1, 100)
                ax.plot(x, y, linewidth=5.0, color=color)
                x = np.linspace(row - 1, row + 1, 100)
                y = np.linspace(line + 1, line - 1, 100)
                ax.plot(x, y, linewidth=5.0, color=color)
            line += 2
            row += 2
        row -= 4
        line = 0
plt.show()