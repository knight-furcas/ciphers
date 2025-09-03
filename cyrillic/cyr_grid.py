import matplotlib.pyplot as plt
import matplotlib as mpl

import numpy as np

code1 = "00000"
slovnik = {chr(1040): code1}
for symb in range(1041, 1072):
    code2 = int(code1, 2) + 1
    code1 = bin(code2)
    slovnik[chr(symb)] = code1[2:]
for i in slovnik:
    while len(slovnik[i]) < 5:
        slovnik[i] = "0" + slovnik[i]

slovnik[" "] = " "

# input
word = input().upper()
listword = []
for i in word.upper():
    if i in slovnik:
        listword.append(i)

if not listword:
    print("ОШИБКА. ТЕКСТ ДОЛЖЕН СОДЕРЖАТЬ КИРИЛЛИЦУ")

fig, ax = plt.subplots(dpi=250)
plt.grid(False)
plt.axis('off')
ax.set_aspect('equal')
fig.patch.set_facecolor('black')

cmap = mpl.colormaps['autumn']
list_colors = cmap(np.linspace(0, 1, len(listword)))

row = 0
line = 0
width = 4
for c, i in enumerate(listword):
    color = list_colors[c]
    if i == " ":
        row += 2
    else:
        for symbol in slovnik[i]:
            if symbol == "0":
                x = np.linspace(row - 1, row + 1, 2)
                y = np.linspace(line - 1, line + 1, 2)
                ax.plot(x, y, linewidth=width, color=color)
                # ax.plot(x1, y1, '-o', linewidth=width, color=color, ms=area, mfc='red')
            else:
                x = np.linspace(row - 1, row + 1, 2)
                y = np.linspace(line + 1, line - 1, 2)
                ax.plot(x, y, linewidth=width, color=color)
                # ax.plot(x1, y1, '-o', linewidth=width, color=color, ms=area, mfc='red')
            line += 2
            row += 2
        row -= 8
        line = 0

plt.show()