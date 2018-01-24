unconfirmed_users = ['brendan', 'laura', 'simona']

confirmed_users = []

while unconfirmed_users :
	current_user = unconfirmed_users.pop()
	print('verifing user: ', current_user.title())
	
	confirmed_users.append(current_user)

