from voter import vdetails
from voterport import VoterManager
from candidate import cdetails
import time
import datetime
from datetime import date
class electioncomm(vdetails,cdetails):
	def election(self):
		voter_id=raw_input("Enter the voter unique voter Id\t")
                if VoterManager.vdict.has_key(voter_id):
			print("choose one of the candidate to vote.... Choose Carefully!!")
			for i in cdict:
				print cdict[i]		
