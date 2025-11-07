n = int(input())
d = [0]*100

d[:10] = [1,1,1,2,2,3,4,5,7,9]

for i in range(10,100):
	d[i] = d[i-2]+d[i-3]

for i in range(n):
	num = int(input())
	print(d[num-1])
