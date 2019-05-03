import os
import json
from tkinter import Tk
from tkinter.filedialog import askopenfilename

envVar = 'GOOGLE_APPLICATION_CREDENTIALS'

def IsCredFileSet():
	if os.getenv(envVar) is not None:
		return True
	else:
		return False

def FindAndSetCred():
	Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
	filename = askopenfilename(title = "Select Google JSON",filetypes = [("Google Credential Files","*.json")]) # show an "Open" dialog box and return the path to the selected file
	if filename != "":
		os.environ[envVar] = filename

def GetProjectName():
	with open(os.environ[envVar], 'r') as file:
		jsonObj = json.loads(file.read().replace('\n', ''))
		return str(jsonObj["project_id"])