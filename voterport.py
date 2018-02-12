from voter import vdetails
class VoterManager:
    vfile = open("vtfile.txt", 'a')
    def voteradd(self):
        vfile = open("vtfile.txt", 'a')
        vfile.write(vdetails.v_id)
        vfile.write(":")
        vfile.write(vdetails.v_name)
        vfile.write("\n")
        return vfile
    def isvalidvoter(self):
         if vdetails.voterinit(self).v_age >= 18:
                vfile = open("vtfile.txt",'r')
                vdict = {}
                for line in vfile:
                    x = line.split(":")
                    vt_id = x[0]
                    vt_name = x[1]
                    vdict[vt_id] = vt_name
                if vdetails.voterinit().v_id in vdict :
                    print("User already exist!!!! \nNot allowed to vote!!")
                else:
                     vtm = VoterManager().voteradd
         else:
            print("not even eligible for voting")