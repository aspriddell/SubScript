import os
import GCloud
import GUI
import pysubs2
import re
import itertools
from google.cloud import translate_v3beta1 as translate

reg = '(?i)(\\\\n)|(\\n)|({.*})' #regex to isolate line breaks and the stage directions \\N and {} (insensitive)

def LoadSubs():
	file = GUI.LoadSubs();
	if file != "":
		subs = pysubs2.load(file, encoding="utf-8") #load subs file

		#get the lang code
		language = GCloud.GetLanguageCode(subs)
		print("Language detected as {}".format(language))

		#list events
		eventcount = len(subs.events)
		currentevent = 0

		for a in subs.events:
			currentevent += 1
			editedlist = list(filter(None, re.split(reg,a.text))) 
			tt = []

			for i in range(0,len(editedlist)):
				if not re.match(reg,str(editedlist[i])):
					tt.append(i)
			a.text = (''.join(GCloud.TranslateSet(editedlist,tt,language,'en-US')))
			GUI.UpdateTranslation(str(round(currentevent/eventcount*100,1))+" %")

		subs.save("subs.ass")
LoadSubs()