name = input("Enter file: ")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name,'r')
count = 0
directory = dict()

for line in handle:
    if line.startswith('From ') :
        divilines = line.split()
        emailsender = divilines[1]
        directory[emailsender] = directory.get(emailsender,0) +1
        count = count + directory[emailsender]


biggestcount = None
biggestsender = None
for emailsender,count in directory.items():
    if biggestcount is None or count > biggestcount:
        biggestsender = emailsender
        biggestcount = count

print(biggestsender, biggestcount)

#Output should be:
#cwen@iupui.edu 5
