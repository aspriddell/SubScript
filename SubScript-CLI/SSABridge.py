import pysubs2
import GUI
import re

reg = '(?i)(\\\\n)|(\\n)|({.*})' #regex to isolate line breaks and the stage directions \\N and {} (insensitive)

def Load():
	file = GUI.LoadSubs();
	if file != "":
		subs = pysubs2.load(file, encoding="utf-8") #load subs file
		for a in subs.events:
			editedlist = list(filter(None, re.split(reg,a.text))) 
			tt = []
			for i in range(0,len(editedlist)):
				if not re.match(reg,str(editedlist[i])):
					tt.append(i)

			print("L: "+str(editedlist) + "T: " + str(tt)) #filter [''] entries
