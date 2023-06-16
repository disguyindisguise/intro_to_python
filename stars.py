# The Stars Project
# Name: Ian Sinza
# This project aims to build one big program that enables users to create star charts (pictures) from star catalog data files. The project is divided into multiple parts, where each part requires functions to be written and tested. All work should be done in a python file called stars.py. As the parts build on top of each other, it is imperative that each part be completed correctly.

from tkinter import *
window = Tk()
canvas = Canvas(window, width=500, height=500, background="black")
canvas.pack()


def getStarPixelX(star_string):
  star_string_list = star_string.split(',')
  x = float(star_string_list[0])
  pixel_x = 250 + (250 * x)
  return pixel_x

def getStarPixelY(star_string):
  star_string_list = star_string.split(',')
  y = float(star_string_list[1])
  return 250 - (250 * y)

def getStarSize(star_string):
  star_string_list = star_string.split(',')
  size = 10.0 / (float(star_string_list[4]) + 2)
  return size

def getStarName(star_string):
  star_string_list = star_string.split(',')
  if len(star_string_list) == 7:
    return str(star_string_list[6])
  else:
    return ''

def drawStar(star_string):
  x = getStarPixelX(star_string)
  y = getStarPixelY(star_string)
  size = getStarSize(star_string)
  x1 = x - (size/2)
  y1 = y + (size/2)
  x2 = x + (size/2)
  y2 = y - (size/2)
  canvas.create_rectangle(x1, y1, x2, y2, fill="white", width=0)

def drawAllStars():
  file = open('stars.txt')
  star_text = file.read()
  star_lines = star_text.split('\n')
  for line in star_lines:
    drawStar(line)

def getStarString(star_name):
  file = open('stars.txt')
  star_text = file.read()
  star_lines = star_text.split('\n')
  for line in star_lines:
    if star_name == getStarName(line):
      return line

def drawStarByName(star_name):
  drawStar(getStarString(star_name))

def drawConstellationLine(star_one, star_two):
  x1 = getStarPixelX(getStarString(star_one))
  y1 = getStarPixelY(getStarString(star_one))
  x2 = getStarPixelX(getStarString(star_two))
  y2 = getStarPixelY(getStarString(star_two))
  canvas.create_line(x1, y1, x2, y2, fill="yellow")

def drawConstellationFile(file_name):
  file = open(file_name)
  const_text = file.read()
  const_lines = const_text.split('\n')
  for const_line in const_lines:
    star_line = const_line.split(',')
    drawConstellationLine(star_line[0], star_line[1])
    
drawAllStars()
drawConstellationFile("BigDipper_lines.txt")
drawConstellationFile("Bootes_lines.txt")
drawConstellationFile("Cas_lines.txt")
drawConstellationFile("Cyg_lines.txt")
drawConstellationFile("Gemini_lines.txt")
drawConstellationFile("Hydra_lines.txt")
drawConstellationFile("UrsaMajor_lines.txt")
drawConstellationFile("UrsaMinor_lines.txt")

mainloop()