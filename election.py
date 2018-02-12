import time
import sys
from voter import vdetails
from voterport import VoterManager
from candidateport import CandidateManager
from datetime import date


el_date = date(2018, 2, 7)
today = date.today()
print("\n")
newvar = 0


def main():
    print("\n---------Welcome To Online Voting Portal---------\n")
    user = input("Who are you?? Choose one of these:\nCandidate-->[C]\nVoter-->[V]\n")
    while user == 'c' or user == 'C' or user == 'v' or user == 'V' or user == 'e' or user == 'E':
        if user == 'V' or user == 'v':
            vtch = input("Add Voter?? [Y/N] \t")
            while vtch == 'y' or vtch == 'Y':
                vt = vdetails()
                vtm = VoterManager()
                vtm.isvalidvoter()
                vtch = input("Add Voter?? [Y/N] \t")
            else:
                user = input("Choose one of these:\nCandidate-->[C]\nVoter-->[V]\nExit---->[E]")
        elif user == 'C' or user == 'c':
            cdch = input("Add Candidate?? [Y/N] \t")
            while cdch == 'y' or cdch == 'Y':
                c_name = input("Enter Candidate Name here:\t")
                c_id = input("Enter Candidate Unique Id here:\t")
                c_aadhar = input("Enter Candidate Unique Aadhar Id here:\t")
                cd = CandidateManager(c_name, c_id, c_aadhar)
                cd.addcndt()
                cdch = input("Add Candidate?? [Y/N] \t")
            else:
                user = input("Choose one of these:\nCandidate-->[C]\nVoter-->[V]\nExit---->[E]")
        elif user == 'E' or user == 'e':
            break
        else:
            print("wrong choice")


if __name__ == "__main__":
    main()

if today == el_date:
    print("Now you are here to Vote........\n")
    vdetails.findvoter()
