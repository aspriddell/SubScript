import os
from tkinter import Tk
from tkinter.filedialog import askopenfilename

def IsCredFileSet():
	try:
		if os.environ['GOOGLE_APPLICATION_CREDENTIALS'] != "":
			return True
		else:
			raise Exception
	except:
		return False


def FindAndSetCred():
	Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
	filename = askopenfilename(title = "Select Google JSON",filetypes = [("Google Credential Files","*.json")]) # show an "Open" dialog box and return the path to the selected file
	if filename != "":
		os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = filename