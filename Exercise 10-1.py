fname = raw_input('Enter file name: ')
try:
	fhandle = open(fname)
except:
	print 'File cannot be opened:', fname
	exit()
emails = dict()
for line in fhandle:
	if line.startswith('From '):
		line = line.split()
		email = line[1]
		emails[email] = emails.get(email,0) + 1
emailslist = []
for email, count in emails.items():
	emailslist.append( (count, email) )
emailslist.sort(reverse=True)
for count, email in emailslist[:1]:
	print email, count