"""
Write your answer for Odd Numbers below here:
"""

def main():
	oddList = []
	n = input('Enter a number to get odds numbers before it: ')
	# n = int(n)
	for i in range(int(n)):
	    if i % 2 == 1:
	        oddList.append(i)
	print(oddList)
	
	# checking the first and last number in oddList
	print('First odd: {} | Last odd: {}'.format(oddList[0], oddList[-1]))
	# counting the length of the list
	print('Total of: {} | Total of odd: {}'.format(n,len(oddList)))

if __name__ == '__main__':
    main()
