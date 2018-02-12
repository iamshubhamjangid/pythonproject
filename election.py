import time
from elctionmanager import electioncomm
import datetime
from voter import vdetails
from voterport import VoterManager
from candidateport import CandidateManager
from datetime import date
el_date = date(2018, 2, 7)
today = date.today()
newvar = 0
def main():
    time=datetime.datetime.now()
    print("\n---------Welcome To Online Voting Portal---------\n")
    if time.hour<=18 and time.hour>=10:
      print("You are in the registration Portal\n Registration will be opoen till 18:00\n")
      user = raw_input("Who are you?? Choose one of these:\nCandidate-->[C]\nVoter-->[V]\n")
      while user == 'c' or user == 'C' or user == 'v' or user == 'V' or user == 'e' or user == 'E':
        if user == 'V' or user == 'v':
            vtch = raw_input("Add Voter?? [Y/N] \t")
            while vtch == 'y' or vtch == 'Y':
                vt = vdetails()
                vtm = VoterManager()
                vtm.isvalidvoter()
                vtch = raw_input("Add Voter?? [Y/N] \t")
            else:
                user = raw_input("Choose one of these:\nCandidate-->[C]\nVoter-->[V]\nExit---->[E]")
        elif user == 'C' or user == 'c':
            cdch = raw_input("Add Candidate?? [Y/N] \t")
            while cdch == 'y' or cdch == 'Y':
                cd= vdetails()
                cdm = CandidateManager()
                cdm.isvalidcandidate()
                cdch = raw_input("Add Candidate?? [Y/N] \t")
            else:
                user = raw_input("Choose one of these:\nCandidate-->[C]\nVoter-->[V]\nExit---->[E]")
        elif user == 'E' or user == 'e':
            print("Now Election Commisioner will announce the election date:...SO please wait!!")
	    elcom=electioncomm()
	    elcom.election()
      else:
            print("wrong choice")
    else:
	print(" Either Voting has Closed!!!\n")
if __name__ == "__main__":
    main()

if today == el_date:
    print("Now you are here to Vote........\n")
                       
