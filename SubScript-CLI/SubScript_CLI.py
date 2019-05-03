import os
import GCloud
import SSABridge
from google.cloud import translate_v3beta1 as translate

def Translate():
	if GCloud.IsCredFileSet() == False:
		GCloud.FindAndSetCred()

	client = translate.TranslationServiceClient()

	project_id = GCloud.GetProjectName()
	text = 'こんにちは'
	location = 'global'

	parent = client.location_path(project_id, location)

	response = client.translate_text(
		parent=parent,
		contents=[text],
		mime_type='text/plain',  # mime types: text/plain, text/html
		source_language_code='ja-JP',
		target_language_code='en-US')

	for translation in response.translations:
		print('Translated Text: {}'.format(translation))

def LoadSubs():
	SSABridge.Load()

LoadSubs()
#Translate();