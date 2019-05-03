import pysubs2
import GUI

def Load():
	file = GUI.LoadSubs();
	if file != "":
		subs = pysubs2.load(file, encoding="utf-8")
		for a in subs.events:
			print(a)