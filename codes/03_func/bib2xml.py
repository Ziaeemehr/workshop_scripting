#THIS REQUIRES THAT bibutils IS INSTALLED ON YOUR MACHINE

"""
Usage:
./Bib2Word2010XML.py [Input file name] [Output file name]
"""

import sys
import fileinput
import os

if __name__ == '__main__':
  #input a BibTex .bib file
  fnameIN = "lib.bib"
  fnameOUT = "lib.xml"

  #run bibutils functions to convert to Word XML
  os.system("bib2xml " + fnameIN + " > TEMPOUT1.xml")
  os.system("xml2wordbib TEMPOUT1.xml > TEMPOUT2.xml")
  os.system("rm TEMPOUT1.xml")

  #clean up for Word 2010 formatting
  f1 = open('TEMPOUT2.xml', 'r')
  f2 = open(fnameOUT, 'w')
  for line in f1:
    line = line.replace("ArticleInAPeriodical", "JournalArticle")
    line = line.replace("PeriodicalName", "JournalName")
    line = line.replace("Proceedings", "ConferenceProceedings")
    f2.write(line)
  f1.close()
  f2.close()
  os.system("rm TEMPOUT2.xml")