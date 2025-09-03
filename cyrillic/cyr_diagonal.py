import matplotlib.pyplot as plt
import matplotlib as mpl

import numpy as np
from itertools import combinations as comb

# alphabet in frequency
ru_freq = "оеаинтсрвлкмдпуяыьгзбчйхжшюцщэфъё"

# creating a dict for vowels
list_of_vowels = "оеаиуяыюэё".upper()

vowels_ciphers = []
for i in range(4):
    vowels_ciphers.append(tuple(str(i)))
ciphers = comb("0123", 2)
for i in ciphers:
    vowels_ciphers.append(i)

dict_vowels = {}
for i, letter in enumerate(list_of_vowels):
    dict_vowels[letter] = vowels_ciphers[i]
    a = ""
    for n in vowels_ciphers[i]:
        a += n

# creating a dict for consonants
list_of_consonants = "нтсрвлкмдпьгзбчйхжшцщфъ".upper()

consonants_ciphers = []
for i in range(4, 10):
    consonants_ciphers.append(tuple(str(i)))
ciphers = comb("456789", 2)
for i in ciphers:
    consonants_ciphers.append(i)
ciphers = comb("456789", 3)
for i in ciphers:
    consonants_ciphers.append(i)

dict_consonants = {}
for i, letter in enumerate(list_of_consonants):
    dict_consonants[letter] = consonants_ciphers[i]
    a = ""
    for n in consonants_ciphers[i]:
        a += n

fig, ax = plt.subplots()
# plt.grid(False)
plt.axis('off')

word = input().upper()

for symbol in word:
    if not symbol in ru_freq.upper() and symbol != " ":
        print("ОШИБКА. ТЕКСТ ДОЛЖЕН СОДЕРЖАТЬ КИРИЛЛИЦУ")

line = 0
width = 1

fig.patch.set_facecolor('black')

cmap = mpl.colormaps['autumn']
list_colors = cmap(np.linspace(0, 1, len(word)))

a = len(word)
for ind, letter in enumerate(word):
    if letter == " ":
        line -= 3
    else:
        color = list_colors[ind]
        if letter in list_of_vowels:
            if ind > 0 and word[ind - 1] in list_of_consonants:
                line += 3
                a -= 1
            for i in range(-2, 1):
                x = np.linspace(-1, 1, 2)
                y = np.linspace(line + i - 1, line + i + 1, 2)
                ax.plot(x, y, linewidth=width, color=color)
            for symbol in dict_vowels[letter]:
                if symbol == "0" or symbol == "1":
                    x1 = np.linspace(1, 1, 2)
                else:
                    x1 = np.linspace(-1, -1, 2)

                if symbol == "0":
                    y1 = np.linspace(line + 1, line, 2)
                elif symbol == "1":
                    y1 = np.linspace(line, line - 1, 2)
                elif symbol == "2":
                    y1 = np.linspace(line - 1, line - 2, 2)
                else:
                    y1 = np.linspace(line - 2, line - 3, 2)
                ax.plot(x1, y1, linewidth=width, color=color)
        else:
            for i in range(-2, 1):
                x = np.linspace(-1, 1, 2)
                y = np.linspace(line + i - 1, line + i + 1, 2)
                ax.plot(x, y, linewidth=width, color=color)
            for symbol in dict_consonants[letter]:
                if symbol == "4":
                    x = np.linspace(1, 2, 2)
                    y = np.linspace(line + 1, line + 2, 2)
                    ax.plot(x, y, linewidth=width, color=color)
                    x = np.linspace(2, 2, 2)
                    y = np.linspace(line + 2, line + 1, 2)
                    ax.plot(x, y, linewidth=width, color=color)
                elif symbol == "5":
                    x = np.linspace(1, 2, 2)
                    y = np.linspace(line, line + 1, 2)
                    ax.plot(x, y, linewidth=width, color=color)
                elif symbol == "6":
                    x = np.linspace(1, 2, 2)
                    y = np.linspace(line - 1, line, 2)
                    ax.plot(x, y, linewidth=width, color=color)
                    x = np.linspace(2, 2, 2)
                    y = np.linspace(line, line + 1, 2)
                    ax.plot(x, y, linewidth=width, color=color)
                elif symbol == "7":
                    x = np.linspace(-2, -1, 2)
                    y = np.linspace(line - 2, line - 1, 2)
                    ax.plot(x, y, linewidth=width, color=color)
                    x = np.linspace(-2, -2, 2)
                    y = np.linspace(line - 2, line - 3, 2)
                    ax.plot(x, y, linewidth=width, color=color)
                elif symbol == "8":
                    x = np.linspace(-2, -1, 2)
                    y = np.linspace(line - 3, line - 2, 2)
                    ax.plot(x, y, linewidth=width, color=color)
                else:
                    x = np.linspace(-2, -1, 2)
                    y = np.linspace(line - 4, line - 3, 2)
                    ax.plot(x, y, linewidth=width, color=color)
                    x = np.linspace(-2, -2, 2)
                    y = np.linspace(line - 4, line - 3, 2)
                    ax.plot(x, y, linewidth=width, color=color)
        line -= 3


ax.set_aspect("equal", adjustable="datalim")
ax.set_box_aspect(a / 5)
ax.autoscale()

plt.show()