import os
import json
import GUI

envVar = 'GOOGLE_APPLICATION_CREDENTIALS'

def IsCredFileSet():
	if os.getenv(envVar) is not None:
		return True
	else:
		return False

def FindAndSetCred():
	filename = GUI.LoadGCloud()
	if filename != "":
		os.environ[envVar] = filename

def GetProjectName():
	with open(os.environ[envVar], 'r') as file:
		jsonObj = json.loads(file.read().replace('\n', ''))
		return str(jsonObj["project_id"])