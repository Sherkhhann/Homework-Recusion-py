def countNum(s, i=0, cnt=0):
	list_new=["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
	if i==len(s):
		return cnt
	if s[i] in list_new:
		cnt+=1
	
	return countNum(s, i+1, cnt)

a=input()
print(countNum(a))

# a=input()
# cnt=0
# listt=["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
# for i in a:
# 	if i in listt:
# 		cnt+=1
# print(cnt)