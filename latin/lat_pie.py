import matplotlib.pyplot as plt
from matplotlib.patches import Wedge
import matplotlib as mpl

import numpy as np
from itertools import combinations as comb


str1 = '12345678'
list_of_comb = list(comb(str1, 2))
for n, i in enumerate(list_of_comb):
    list_of_comb[n] = f'{i[0]}{i[1]}'
dict_of_symb = dict()

for i in range(65, 91):
    dict_of_symb.update({chr(i): list_of_comb[i - 65]})

word = input().upper()

for symbol in word:
    if not symbol in dict_of_symb.keys() and symbol != ' ':
        print("error. available characters: latin".upper())

fig, ax = plt.subplots(layout='constrained')
ax.set_aspect("equal", adjustable="datalim")
ax.set_box_aspect(1)
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)
plt.grid(False)
plt.axis('off')
plt.xlim(-len(word) - 4, len(word) + 4)
plt.ylim(-len(word) - 4, len(word) + 4)

fig.patch.set_facecolor('black')

cmap = mpl.colormaps['autumn_r']
list_colors = cmap(np.linspace(0, 1, len(word)))

width = 3

for i in range(len(word) - 1, -1, -1):
    if word[i] == ' ':
        ax.add_artist(mpl.patches.Circle((0, 0), i + 2, facecolor=[0, 0, 0], edgecolor=list_colors[i], linewidth=width))
    else:
        sequence = dict_of_symb[word[i]]
        if abs(int(sequence[0]) - int(sequence[1])) > 4: sequence = f"{sequence[1]}{sequence[0]}"
        draw = Wedge((0, 0), i + 2, (int(sequence[0]) - 1) * 45, (int(sequence[1]) - 1) * 45, facecolor=[0, 0, 0],
                     edgecolor=list_colors[i], linewidth=width)
        ax.add_artist(draw)

for i in range(1, 9):
    ax.add_artist(Wedge((0, 0), len(word) + 3, (i - 1) * 45, (i * 45), color='yellow', linewidth=0.1, linestyle='--', fill=False))
    plt.text((len(word) + 4) * np.cos(np.radians((i - 1) * 45)), (len(word) + 4) * np.sin(np.radians((i - 1) * 45)),
             str(i), size=15, color='yellow')

ax.add_artist(mpl.patches.Circle((0, 0), 1, facecolor=[0, 0, 0], edgecolor=list_colors[1], linewidth=width))

plt.show()