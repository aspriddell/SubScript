import os
import GCloud

if GCloud.IsCredFileSet() == False:
	GCloud.FindAndSetCred()
