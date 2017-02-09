

def isDebug():
	return(True)

def log(info):
	if isDebug():
		try:
			print(info)
		except:
			print(info.encode("UTF-8"))
