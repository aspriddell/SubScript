from tkinter import Tk
from tkinter.filedialog import askopenfilename
from termcolor import colored

Tk().withdraw()

def LoadGCloud():
	return askopenfilename(title = "Select Google JSON",filetypes = [("Google Credential Files","*.json")]) # show an "Open" dialog box and return the path to the selected file

def LoadSubs():
	return askopenfilename(title = "Select Subs",filetypes = [("ASS","*.ass"),("SSA","*.ssa")]) # show an "Open" dialog box and return the path to the selected file

def Clean():
	print('\n'*50)

def UpdateTranslation(progress):
	Clean()
	print(colored('Translating: ', 'orange') +colored(progress, 'green'))

def SaveSubs():
	return tkFileDialog.asksaveasfilename(defaultextension = ".ass", filetypes = [("ASS","*.ass"),("SSA","*.ssa")], title = "Select Output File")