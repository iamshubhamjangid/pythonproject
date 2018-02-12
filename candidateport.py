class CandidateManager:
    cCount = 0
    def __init__(self, c_name, c_id, c_aadhar):
        self.c_name = c_name
        self.c_id = c_id
        self.c_aadhar = c_aadhar
        CandidateManager.cCount += 1
        cdict={c_name:c_id}
    def displayCount(self):
        print ("Total Candidates are: %d" % CandidateManager.cCount)
    def displayCandidate(self):
        print ("Name : ", self.c_name,  ", Voter Id ", self.c_id,  ", Aadhar Id: ", self.c_aadhar)
    def addcndt(self):
        c_age = int(input("Enter Candidate Age here\t"))
        if c_age>=28:
            cfile = open("cdfile.txt",'r')
            cdict={}
            for line in cfile:
                x = line.split(":")
                cd_id = x[0]
                cd_name = x[1]
                cdict[cd_id] = cd_name
            if self.c_id in cdict:
                print("User already exist!!!! \nNot allowed to Add multiplae same candidates!!!")
            else:
                cfile=open("cdfile.txt",'a')
                cfile.write(self.c_id)
                cfile.write(":")
                cfile.write(self.c_name)
                cfile.write("\n")
                print(cfile)
        else:
            print("Not even eligible for vote")
