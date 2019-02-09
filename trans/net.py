import socket
import time
hostname = "www.google.com"
arr = []

def to_connected():
	try:
		host = socket.gethostbyname(hostname)
		s = socket.create_connection((host, 80), 2)
		return arr.append(True)
	except:
		pass
	return arr.append(False)

def is_connected():
	count = 0
	for i in range (20):
		to_connected()
	for i in arr:
		if i == True:
			count=count+1
	if count>=15:
		return True
	else:
		return False		

if __name__=="__main__":
		start_time = time.time()
		flag=is_connected()
		print (flag)
		print("--- %s seconds ---" % (time.time() - start_time))
		#time.sleep(0.1)
		print(arr)	
