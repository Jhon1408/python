n = int(input())
for x in xrange(0,n):
	n=int(input())
	result=0
	p=5
	while p<=n:
		result+=n//p
		p*=5
	print(result)