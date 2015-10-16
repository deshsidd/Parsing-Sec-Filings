import re

pattern1 = re.compile(r"CONSOLIDATED STATEMENTS? OF CASH FLOWS[\s\n]+<TABLE>.+?<\/TABLE>" ,re.S )
pattern2 = re.compile(r"CONSOLIDATED STATEMENTS OF CASH FLOWS.+?<\/(TABLE|table)>" ,re.S )
pattern3 = re.compile(r"Consolidated Statements of Cash Flows<BR>.+?<\/(TABLE|table)>" ,re.S | re.IGNORECASE )
pattern4 = re.compile(r"Consolidated Statements of Cash Flows</B>.+?<\/(TABLE|table)>" ,re.S | re.IGNORECASE )
#Consolidated Statements of Cash Flows</B>
ctr=0

for i in range(1,101,1):
	ifile1 = open('files/'+ str(i) +'.txt', 'r')
	ifile2 = open('files/'+ str(i) +'.txt', 'r')
	ifile3 = open('files/'+ str(i) +'.txt', 'r')
	ifile4 = open('files/'+ str(i) +'.txt', 'r')
	ofile = open('output/table'+ str(i) +'.txt', 'w')

	table = re.search(pattern1,ifile1.read())

	if table == None :
		table1 = re.search(pattern2,ifile2.read())
		if table1 != None :
			ofile.write(table1.group(0))
		else :
			table2 = re.search(pattern3,ifile3.read())
			if table2 != None :
				ofile.write(table2.group(0))
			else :
				table3 = re.search(pattern4,ifile4.read())
				if table3 != None :
					ofile.write(table3.group(0))
				else :

					ofile.write('no table found')
					ctr=ctr+1
					print i
	else :
		ofile.write(table.group(0))

	ifile1.close()
	ifile2.close()
	ofile.close()

print ctr





# Close opend file



