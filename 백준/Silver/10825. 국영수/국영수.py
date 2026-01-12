import sys
input = sys.stdin.readline

n = int(input())
students = []

for i in range(n):
    name, korea, english, math = input().split()
    students.append([name,int(korea),int(english),int(math)])

students.sort(key = lambda x:[-x[1],x[2],-x[3],x[0]])

for s in students:
    print(s[0])