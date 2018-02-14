class votermgr:
    def __init__(self,name,aadhar,vid,age):
	self.v_name=name
	self.v_age=age
	self.v_id=vid
	self.v_aadhar=aadhar

    def isValid(self):
	if self.v_age>=18:
	    return True
	else:
	    print("You are not satisfying the minimum requirements to vote!!!\n You are under 18!!")

    def addvoter(self,name,vid):
	global voterdict
	voterdict={vid:name}
	return voterdict

    def deletevoter(self,vid):
	del voterdict[vid]
	return voterdict

    def displayvoter(self):
	print voterdict

	
	
