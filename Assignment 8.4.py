#Paragraph is the poem;
#wordpieces turns the paragragh into lines;
#now have to figure out how to get the lines into individual words!
#This is done by 'looping over the split' aka lines 17 & 18;
#to get one word at a time.
#poemempty - is the empty list
#RECALL for line 19 - If x in poemempty : continue
#continue jumps back to the top of the loop; hence if x
#is NOT in the empty list it will be added!
#Line 25 sorts then prints the list.

fname = input("Enter file name: ")
fh = open('romeo.txt','r')
paragraph = fh
poemempty = list()

for line in paragraph:
    delimiter = ' '
    wordpieces = line.split(delimiter)
    for x in line.split():
        if x in poemempty : continue
        poemempty.append(x)


print(sorted(poemempty))


#Output should be:
#['Arise', 'But', 'It', 'Juliet', 'Who', 'already', 'and', 'breaks', 'east', 'envious', 'fair', 'grief', 'is', 'kill', 'light', 'moon', 'pale', 'sick', 'soft', 'sun', 'the', 'through', 'what', 'window', 'with', 'yonder']
