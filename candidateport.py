from candidate import cdetails
class CandidateManager(cdetails):
    cfile = open("cdfile.txt", 'a')
    def candidateadd(self):
	cd=cdetails()
        cfile = open("cdfile.txt", 'a')
        cfile.write(cnd_id)
        cfile.write(":")
        cfile.write(cd.candidateinit())
        cfile.write("\n")
        print(cfile)
    def isvalidcandidate(self):
         cdt=cdetails()
         if cdt.candidateage()>= 28:
                cfile = open("cdfile.txt",'r')
                global cdict
		cdict = {}
                for line in cfile:
                    x = line.split(":")
                    cndt_id = x[0]
                    cndt_name = x[1]
                    cdict[cndt_id] = cndt_name
		global cnd_id
		cnd_id=cdt.cdidaadhar()
                if cdict.has_key(cnd_id) :
                    print("Candidate already exist!!!! \nNot allowed to Add Multiple Same Candidates!!")
                else:
                     cdm=CandidateManager()
		     cdm.candidateadd()
         else:
            print("not even eligible for Apply for Candidate!!")
