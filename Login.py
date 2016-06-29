import console

logins = ['403287','Illusion','Spark']
passwords = ['riseas','superman','batman']

def login():
	login = console.login_alert('Please sign in')
	
	if login[0] in logins:
		loginConfirm = True
	else:
		loginConfirm = False 
	if login[1] in passwords:
		passwordConfirm = True
	else:
		passwordConfirm = False 
		
	if loginConfirm == True and passwordConfirm == True:
		console.alert('Welcome!')
	else:
		console.alert('Access denied')
		
login()
