import pysubs2
import GUI
import re

def Load():
	file = GUI.LoadSubs();
	if file != "":
		subs = pysubs2.load(file, encoding="utf-8") #load subs file
		for a in subs.events:
			listofparts = str(a.text).split('\\N') #split newline
			editedlist = []
			for x in range(0,len(listofparts)):
				editedlist.append(listofparts[x]) #add to new list
				if x < len(listofparts)-1: #ignore the last part
					editedlist.append('\n') #add newline char
			editedlist = list(filter(None, editedlist))
			print("O: "+a.text+" | E: "+str(editedlist)) #filter [''] entries
