from voter import voter
class VoterManager:
    vfile=open("vtfile.txt",'a')
    def voteradd(self):
          vfile=open("vtfile.txt",'a')
          vfile.write(voter.v_id)
          vfile.write(":")
          vfile.write(voter.v_name)
          vfile.write("\n")
          print(vfile)
    def isvalidvoter(self):
          vt=voter()
          if vt.v_age>=18:
            vfile=open("vtfile.txt",'r')
            vdict={}
            for line in vfile:
              x=line.split(":")
              vt_id=x[0]
              vt_name=x[1]
              vdict[vt_id]=vt_name
            if vdict.has_key(vt.v_id):
              print("User already exist!!!! \nNot allowed to vote!!")
            else:
              vtm=VoterManager().voteradd()
	        else:
            print("not even eligible for voting")