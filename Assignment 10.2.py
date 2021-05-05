name = input("Enter file: ")
if len(name) < 1: name = "mbox-short.txt"
handle = open(name)

distmessages = dict()

for line in handle:
    if line.startswith('From '):
        divilines = line.split()
        time = divilines[5]
        delimiter = ':'
        hrminsec = time.split(delimiter)
        hour = hrminsec[0]
        distmessages[hour] = distmessages.get(hour, 0) + 1

msgperhrlist = list()
for hour, count in distmessages.items():
    msgperhrlist.append((hour, count))

output = sorted(msgperhrlist)

for hour, count in sorted(msgperhrlist):
    print(hour, count)


#Output should be:
#04 3
#06 1
#07 1
#09 2
#10 3
#11 6
#14 1
#15 2
#16 4
#17 2
#18 1
#19 1