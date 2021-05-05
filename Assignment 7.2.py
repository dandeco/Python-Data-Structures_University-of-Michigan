#SPOILER ALERT - MY CODE WAS NOT ACCEPTED BY THE AUTOGRADER,
#AS IT GAVE A RESULT OF 0.07338518518519
#WHEN THE OUTPUT IS SUPPOSED TO BE 0.7507185185185187

# Use the file name mbox-short.txt as the file name

fname = input("Enter file name: ")
fh = open('mbox-short.txt', 'r')
count = 0
nottotal = 0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count = count + 1
    findfloat = line.find(':')
    extractnum = line[findfloat + 1:]
    extractfloat = float(extractnum)
    nottotalfloat = float(nottotal)
    total = nottotalfloat + extractfloat
    grandtotal = total + extractfloat

avg = grandtotal / count
print("Average spam confidence:", avg)
