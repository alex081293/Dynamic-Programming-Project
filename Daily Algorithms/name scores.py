'''
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 x 53 = 49714.

What is the total of all the name scores in the file?
'''

fileReading = open('names.txt', 'r')

names = fileReading.read()

nameList = names.split('","')
nameList.sort()
total = 0

for i in xrange(0, len(nameList)):
	value = 0

	name = list(nameList[i])

	for j in xrange(0, len(name)):
		tempV = ord(name[j]) - 64 
		if (tempV > 0 and tempV <= 26):
			value = value + tempV
	if (nameList[i] == 'COLIN'):
		print value
		print i

	total = total + (value * (i+1))

print total