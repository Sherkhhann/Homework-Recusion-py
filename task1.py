def maxNum(a, maxx=-999): 	
	if int(a) < 10 and int(a) < maxx:
		return maxx
	number=int(a)%10
	if number>maxx:
		maxx=number
	return maxNum(int(a)//10, maxx)

a=input()
print(maxNum(a))