from Candidate import Candidate
class candidatemgr(Candidate):
    cddict={}
    def isValid(self,object):
	if self.c_age>=28:
            if candidatemgr.cddict.has_key(self.c_id):
	       print "User already exists!!!\n Not allowed to store multiple Same!!"
	    return True
	else:
	    print("You are not satisfying the minimum requirements to be a candidtae!!!\n You are under 28!!")
   
    def add(self,object):
	candidatemgr.cddict[self.cid]=self.name
	return candidatemgr.cddict

    def delete(self,object):
	del candidatemgr.cddict[self.cid]
	return candidatemgr.cddict

    def listcandidate(self):
	print candidatemgr.cddict

    
