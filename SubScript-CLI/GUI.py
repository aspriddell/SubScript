from tkinter import Tk
from tkinter.filedialog import askopenfilename

Tk().withdraw()

def LoadGCloud():
	return askopenfilename(title = "Select Google JSON",filetypes = [("Google Credential Files","*.json")]) # show an "Open" dialog box and return the path to the selected file

def LoadSubs():
	return askopenfilename(title = "Select Subs",filetypes = [("SSA","*.ssa"),("ASS","*.ass")]) # show an "Open" dialog box and return the path to the selected file