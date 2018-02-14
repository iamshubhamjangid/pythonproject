from vtrmgr import votermgr
def main():
    print("\n---------Welcome To Online Voting Portal---------\n")
    print("You are in the registration Portal\n Registration will be opoen till 18:00\n")
    user = raw_input("Who are you?? Choose one of these:\nCandidate-->[C]\nVoter-->[V]\n")
    while user == 'c' or user == 'C' or user == 'v' or user == 'V' or user == 'e' or user == 'E':
          if user == 'V' or user == 'v':
              vtch = raw_input("Add Voter?? [Y/N] \t")
	      while vtch=='y' or vtch=='Y':
    	          name=raw_input("Enter your name here\t")
                  age=int(input("Enter your age here\t"))
                  vid=raw_input("Enter your unique voter id here\t")
                  aadhar=raw_input("Enter your aadhar number here\t")          
                  vtr=votermgr(name,aadhar,vid,age)
                  if vtr.isValid()==True :
	              vtr.addvoter(name,vid)
		      vtr.displayvoter()
		  vtch = raw_input("Add Voter?? [Y/N] \t")
    
if __name__ == "__main__":
    main()
