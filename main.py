import random
import webbrowser
import os
import re

drives = [ chr(x) + ":" for x in range(65,91) if os.path.exists(chr(x) + ":") ]

paths_to_library = []
MAX_DEPTH = 2

for drive in drives :
	if os.path.isdir(drive + "\Program Files (x86)\Steam\steamapps"):
		paths_to_library.append( drive + "\Program Files (x86)\Steam\steamapps")
	else :
		stuff = drive + "\\"
		for root, dirs, files in os.walk(stuff,topdown=True):
			if (len(root.split("\\")) > MAX_DEPTH) :
				del dirs[:]
			if "steamapps" in dirs : 
				print(root)

				paths_to_library.append(root + "\steamapps")

if(len(paths_to_library) < 1) :
	raise "No games found"

print ("Games Found!")

ids = []

for path_to_library in paths_to_library :
	files = os.listdir(path_to_library)

	for file in files:
		appids = re.findall("\d+",file)
		if (len(appids) > 0) :
			appid = appids[0] 
			ids.append(appid);

id = ids[random.randint(0, len(ids) - 1)]

print("Opening appid : " + id)
webbrowser.open("steam://rungameid/"+id)