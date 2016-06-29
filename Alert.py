import  console

def alert(title,message,button1Title,button2Title):
	a = console.alert(title,message,button1=button1Title,button2=button2Title)
	return a
	
print(alert('Hello','Wassup','Hi','Bye'))

