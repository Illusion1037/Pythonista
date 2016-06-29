def read(file):
	f = open(file,'r')
	return f.read()
	f.close()
	
def write(file,text=''):
	f = open(file,'w')
	f.write(text)
	f.close()
	
def append(file,text):
	f = open(file,'a')
	f.write(text)
	f.close()
