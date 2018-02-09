from voterdetails import voterdtl
class votermgr:
	vt=voterdtl()
	vfile=open("vtfile.txt",'a')
	def voteradd(self):
		vfile=open("vtfile.txt",'a')
		vfile.write(vt.v_id)
		vfile.write(":")
		vfile.write(vt.v_name)
		vfile.write("\n")
		print(vfile)
	def isvalidvoter(self):
		if vt.v_age>=18:
			vfile=open("vtfile.txt",'r')
			vdict={}

	