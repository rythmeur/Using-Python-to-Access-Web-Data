import re
hand = open('regex_sum_171033.txt')
numlist = []
for line in hand:
    line = line.rstrip()
    stuff = re.findall('[0-9]+', line)
    if len(stuff) == 0 :  continue
    # num = float(stuff[0])
    numlist =  stuff + numlist

    # numlist.append(num)
    # print ("numlist  ",len(numlist), numlist)
z= [float(num) for num in numlist]
print ('Sum:', sum(z))

