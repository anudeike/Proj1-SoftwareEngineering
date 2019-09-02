import math
import re

"""
Assumptions:
- Input File contains two integers
- First int is the left margin
- Second int is the right margin
- Every single line is 80 characters
- 1 blank between sentences and 
  1 blank between words
- negative margins will return an error
- 1 inch = 12 characters (including spaces)
- Does not work of the margins are too tight (will alert the user)

Assume that the data is supposed to be coming from a file that we can fill the output program
With these margins in mind, your program should process the remaining text in the file. The program should include as many words as can “fit” between the margins. No words should extend beyond the right margin.

Algorithim: print out to a file and/or in the console the text with appropiate margins

"""

# input file paths
input_path = "input_text.txt"
margins_path = "margins.txt"

# using regex
def addSpaceAfterSentence(s):
  """
  Add's Spaces to the end of a sentence (or after any periods)

  Args: 
    param1: the string to be edited
  
  Returns:
    The resulting string after edits
  """

  return re.sub(r'\.(?! )', '.  ', s)

def readFile(path):
  """
  Reads the file. Will run differently if the file contains margin notation

  Args:
    param1: path to target file

  Returns: 
    Returns a string that contains the file's contents 
  """
  data = ""

  # open the file
  with open(path) as f:
    data = f.read()

  # print(len(list(data)))

  data = addSpaceAfterSentence(data)
  data = data.replace('\n', " ")
  # print(data)

  return data

def setMargins(path, delimiter=":"):
  """
  Reads a margins file: if the file is not formatted correctly, it will
  raise a TypeError

  Args: 
    param1: path to target file
    param2: delimiter for the margins file. Default is `:` but user can specify a custom delimiter
  
  Returns: 
    a margin object (or dictionary in python)

  Raises:
    TypeError: Will raise if in the input file is not inputted correctly
  """

  # create the margins object
  margins = {
    "LEFT": 0,
    "RIGHT": 0
  }

  # open (and close) the file
  # parse the margins file
  with open(path) as mf:
    rawData = mf.read().split(delimiter)
    margins["LEFT"] = rawData[1]
    margins["RIGHT"] = rawData[3]
  
  if int(margins["LEFT"]) < 0 or int(margins["RIGHT"]) < 0:
    raise ValueError("Cannot have negative margins")

  # print(margins)
  return margins

# write the out put
def writeOutput(marginDict, inputString):
  """
  Args:
    param1: margins object specifying the margins of the document
    param2: the input file string
  
  Returns: 
    A correctly formatted array of strings for each line
  """

  document = []

  # find the size of the margin - 1 inch = 12 characters
  left_margin = int(marginDict["LEFT"]) * 12
  right_margin = int(marginDict["RIGHT"]) * 12

  # if the margins are bigger than 80 then the program stops running
  if(left_margin + right_margin >= 80):
    print("No output. Margins are too large.")
    return

  line_length = 80-left_margin-right_margin

  # each line is at most 80 characters long
  for ind in range(1, math.ceil(len(inputString) / line_length)):
    line = " " * left_margin  # create a line of spaces to act as the left margin 

    # if the ind * the line length is greater than the inputString then 
    # set the end slice term to the length
    if((ind * line_length) > len(inputString)):
      line = line + inputString[(ind-1) * line_length: len(inputString)]
      line = line + " " + right_margin

      return 

    line = line + inputString[(ind-1) * line_length:ind * line_length]
    line = line + " " * right_margin
    print(line)
    # print(len(line))
    # document.append(line)
  

  # print(document)

  


  pass
# runner code

customMargins = setMargins(margins_path) # set the margins
input_text = readFile(input_path) # get the input text
writeOutput(customMargins, input_text) # write the output to the console







