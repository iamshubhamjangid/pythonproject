from voter import vdetails
class VoterManager(vdetails):
    vfile = open("vtfile.txt", 'a')
    def voteradd(self):
	vt=vdetails()
        vfile = open("vtfile.txt", 'a')
        vfile.write(vtr_id)
        vfile.write(":")
        vfile.write(vt.voterinit())
        vfile.write("\n")
        print(vfile)
    def isvalidvoter(self):
         vtr=vdetails()
         if vtr.voterage()>= 18:
                vfile = open("vtfile.txt",'r')
                global vdict
		vdict = {}
                for line in vfile:
                    x = line.split(":")
                    vt_id = x[0]
                    vt_name = x[1]
                    vdict[vt_id] = vt_name
		global vtr_id
		vtr_id=vtr.vtidaadhar()
                if vdict.has_key(vtr_id) :
                    print("User already exist!!!! \nNot allowed to vote!!")
                else:
                     vtm=VoterManager()
		     vtm.voteradd()
         else:
            print("not even eligible for voting")
