"""
 Markdown.py
 0. just print whatever is passed in to stdin
 0. if filename passed in as a command line parameter, 
    then print file instead of stdin
 1. wrap input in paragraph tags
 2. convert single asterisk or underscore pairs to em tags
 3. convert double asterisk or underscore pairs to strong tags

"""

import fileinput
import re

blockq = False

def convertStrong(line):
  line = re.sub(r'\*\*(.*)\*\*', r'<strong>\1</strong>', line)
  line = re.sub(r'__(.*)__', r'<strong>\1</strong>', line)
  return line

def convertEm(line):
  line = re.sub(r'\*(.*)\*', r'<em>\1</em>', line)
  line = re.sub(r'_(.*)_', r'<em>\1</em>', line)
  return line

def convertH1(line):
  line = re.sub(r'^#{1}([^#]*)$', r'<h1>\1</h1>', line)
  return line
  
def convertH2(line):
  line = re.sub(r'^#{2}([^#]*)$', r'<h2>\1</h2>', line)
  return line 
  
def convertH3(line):
  line = re.sub(r'^#{3}([^#]*)$', r'<h3>\1</h3>', line)
  return line

def convertBlockquote(line):
  global blockq
  if(not(blockq)):
    if(line.find("> ")):
      blockq = True
      line = re.sub(r'>(.*)', r'<blockquote>\\n\1', line)
  else:
    if (line.find("> ")):
      line = re.sub(r'>(.*)', r'\1', line)
    else:
      blockq = False
      line = re.sub(r'(.*)', r'\1\\n</blockquote>', line)

  return line

    
for line in fileinput.input():
  line = line.rstrip()
  line = convertStrong(line)
  line = convertEm(line)
  line = convertH1(line)
  line = convertH2(line)
  line = convertH3(line)

  special_cases = "<h1>", "<h2>", "<h3>", "<blockquote>", "</blockquote>"
  if(not(any(substring in line for substring in special_cases))):
    print '<p>' + line + '</p>'
  else:
    print line



