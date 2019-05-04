import os, GCloud, GUI, pysubs2, re, itertools, time, colorama
from google.cloud import translate_v3beta1 as translate
from termcolor import *

reg = '(?i)(\\\\n)|(\\n)|({.*})' #regex to isolate line breaks and the stage directions \\N and {} (insensitive)
validoptons = [1,2,3,4]
outlang = 'en-US'
colorama.init()

def LoadSubs():
	GUI.Clean()
	print("Select a file in the dialog that will appear")
	file = GUI.LoadSubs();
	if file != "":
		subs = pysubs2.load(file, encoding="utf-8") #load subs file
		#get the lang code
		language = GCloud.GetLanguageCode(subs)
		print("Language detected as {}".format(language))

		#list events for % GUI updater
		eventcount = len(subs.events)
		currentevent = 0

		print(f"Loaded file with {eventcount} Events and a predicted language of {langauge}")
		input("Press Enter to start the translation...")
		GUI.Clean()
		starttime = time.time()
		for a in subs.events:
			currentevent += 1
			editedlist = list(filter(None, re.split(reg,a.text))) #get rid of None entries
			tt = []

			for i in range(0,len(editedlist)):
				if not re.match(reg,str(editedlist[i])): #decide weather it's worth translating
					tt.append(i)
			a.text = (''.join(GCloud.TranslateSet(editedlist,tt,language,outlang))) #recompile the translated segments
			GUI.UpdateTranslation(str(round(currentevent/eventcount*100,1))+"% | "+str(time.time()-starttime)+" Elapsed") #update UI

		subs.save("subs.ass") #save file

def SetCreds():
	GCloud.FindAndSetCred()
	if GCloud.IsCredFileSet():
		print("Success!")
		time.sleep(2)

def SetOutput():
	GUI.Clean()
	newlanguage = input("Enter the ISO code for the output language (Looks like: en-US): ")
	print()

def Menu():
	while True:
		option = -1
		while option not in validoptons:
			GUI.Clean()
			print("SubScript 0.1 (Beta)")
			print("--------------------")
			print("Options:")

			if GCloud.IsCredFileSet() == False:
				print(colored("1. Set GCloud Service Account Credential File (Not Set)", 'red'))
			else:
				print(colored(f"1. Set GCloud Service Account Credential File (Project: {GCloud.GetProjectName()})",'green'))
			
			print(f"2. Set Translated Output Language (Currently {outlang})")
			print("3. Translate SSA/ASS File")
			print("4. Quit")

			##print rest here
			try:
				option = int(input("\n\nSelect an Option: "))
			except:
				option = -1
		if option == 1:
			SetCreds()
		elif option == 2:
			SetOutput()
		elif option == 3:
			if GCloud.IsCredFileSet():
				LoadSubs()
		elif option == 4:
			break


Menu()