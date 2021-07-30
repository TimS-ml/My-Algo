# https://github.com/pwaller/pyfiglet/tree/master/pyfiglet/fonts
# https://www.cnblogs.com/Python666/p/7289482.html
# https://stackoverflow.com/questions/9632995/how-to-easily-print-ascii-art-text

from pyfiglet import Figlet, FigletFont

all_fonts = FigletFont().getFonts()
print(len(all_fonts), int(len(all_fonts) / 2))

# for i in range(len(all_fonts)):
#     print(all_fonts[i], '\n')
#     f = Figlet(font=all_fonts[i])
#     print(f.renderText("Chilling"))

# for i in range(int(len(all_fonts)/2), len(all_fonts)):
#     print(all_fonts[i], '\n')
#     f = Figlet(font=all_fonts[i])
#     print(f.renderText("LeetCode"))

# my_fonts = [
#     '5lineoblique', '6x10', 'avatar', 'basic', 'big', 'bulbhead', 'chunky',
#     'cli8x8', 'colossal', 'contessa', 'cursive', 'defleppard', 'doom',
#     'fourtops', 'graffiti', 'isometric1', 'rozzo', 'rowancap', 'ogre',
#     'whimsy', 'utopiabi', 'utopiab', 'straight', 'stop', 'standard',
#     'stampatello', 'speed', 'smslant', 'smisome1', 'slscript', 'slant', 'short'
# ]
# print(len(my_fonts))

# for i in range(len(my_fonts)):
#     print(my_fonts[i], '\n')
#     f = Figlet(font=my_fonts[i])
#     print(f.renderText("VENI VIDI VICI"))

# for test
f = Figlet(font='whimsy')  # italic / contessa / basic
print(f.renderText("My-Paper"))
