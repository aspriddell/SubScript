import os
import json
import GUI
import pysubs2
from google.cloud import translate_v3beta1 as translate

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


def GetLanguageCode(subs):
	text = []
	for x in range(0,7):
		text.append(subs.events[x].text)

	if IsCredFileSet() == False:
		FindAndSetCred()

	client = translate.TranslationServiceClient()
	project_id = GetProjectName()
	location = 'global'
	parent = client.location_path(project_id, location)
	response = client.detect_language(
		parent=parent,
		content=' '.join(text),
		mime_type='text/plain')  # mime types: text/plain, text/html
	z = sorted(response.languages, key=lambda x:x.confidence) #get highest confidence language
	return z[0].language_code

def TranslateSet(segments,totranslate,inputlang,outputlang):
	if IsCredFileSet() == False:
		FindAndSetCred()

	parts = segments

	client = translate.TranslationServiceClient()
	project_id = GetProjectName()
	location = 'global'
	parent = client.location_path(project_id, location)

	translatedsegments = []

	for x in range(0,len(totranslate)):
		response = client.translate_text(
			parent=parent,
			contents=[segments[totranslate[x]]],
			mime_type='text/plain',
			source_language_code=inputlang,
			target_language_code=outputlang)

		parts[totranslate[x]] = response.translations[0].translated_text
	
	return parts