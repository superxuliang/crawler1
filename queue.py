








def createQueue(queue_name, type = "SQL"):
	if type == "SQL":
		from sql_queue import SQLQueue
		return(SQLQueue(queue_name))
	else:
		return(None)


#col1: link
#col2: ref
#col3: priority 
#col4: status (1: InQuere 2:deleted 3: using)
#col5: other_infos(json info)

def testQueue():

	a = createQueue("test3")

	print(a.find("abc"))

	print(a.putItems(["abc","def"]))


	print(a.find("abc"))

	print(a.popItems(1))

testQueue()