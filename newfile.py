password = "hakoona matata"
guess_count = 5

while guess_count>0:
	print("Attempt left : " + str(guess_count))
	guess=input("Enter password : ")
	if guess == password:
		print("Great!!! System UNLOCKED!")
		break
	elif guess == "":
		print("Please enter a valid password!")
		guess_count+=1
	elif guess_count==1:
	        print("SYSTEM BLOCKED!")
	        forgot = input("Forgot password? ")
	        reset = input("Wanna reset password? ")
	        newp = input("Enter a new password : ")
	        password = newp
	        guess_count = 6
	else:
	        print("No! Try again!")
	guess_count -= 1
