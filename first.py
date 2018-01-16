choice = raw_input("Enter the choice as Do you want to vote? Y/N")
voter={}
namo=0
raga=0
candidate={'BJP':"NARENDRA D MODI",'Congress':"RAHUL GANDHI"}
while choice == 'y' or choice == 'Y': 
  age= int(input("Enter your age"))
  if age >= 18:
      print("you are eligible for voting in India")
      v_id=raw_input("Enter you unique id")
      aadhar=raw_input("Enter you Unique Aadhar Number")
      voter_id=v_id
      if voter.has_key(voter_id):
        print("User Already Exist!!!!\n NOT ALLOWED TO VOTE!!")
      else:
        voter[voter_id]=aadhar
	print("Now you have the following candidates for voting:-")
	for cd in candidate:
	  print(candidate[cd])
	  print("")
	vote=raw_input("Now Enter the choice as:\n A) Narendra D Modi \n B)Rahul Gandhi\n")
	if vote =='a' or vote =='A':
	   print("Thank you for Voting!!!")
	   namo+=1
	elif vote =='b' or vote =='B':
	   print("Thank you for Voting!!!")
	   raga+=1
	else:
	   print("Please do select the right option form the above choices!!!")
      choice = raw_input("Enter the choice as Do you want to vote? Y/N")
  else:
     print("You are not eligible to vote!!")
     print("exiting.....")
     choice = raw_input("Enter the choice as Do you want to vote? Y/N")
else:
   print("The Users available in the dictionary is:")
   print(voter)
   print("The final selected winner is:-----\n")   	   
   if namo>raga:
	print("\n--------------------Narendra D Modi----------------------")
	print("number of votes=", namo)
	print("\n")
   elif namo<raga:
	print("\n--------------------Rahul Gandhi----------------------")
	print("number of votes=", raga)
	print("\n")
   else:
        print("There is a tie!!!\nso now it will  be decided by the election commisioner!!!")













