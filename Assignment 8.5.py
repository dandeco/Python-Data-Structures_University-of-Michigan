# diviparts - 'parsing'/dividing line into parts aka splitting.
# extractaddress - getting 2nd word aka email address from the line.

fname = input("Enter file name: ")
if len(fname) < 1: fname = "mbox-short.txt"

fh = open(fname, 'r')
count = 0

for line in fh:
    if line.startswith('From:'): continue

    if line.startswith('From'):
        diviparts = line.split()
        extractaddress = diviparts[1]
        print(extractaddress)
        count = count + 1

print("There were", count, "lines in the file with From as the first word")
