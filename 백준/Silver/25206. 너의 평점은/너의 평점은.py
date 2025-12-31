grade = {"A+":4.5,"A0":4.0,"B+":3.5,"B0":3.0,"C+":2.5,"C0":2.0,"D+":1.5,"D0":1.0,"F":0.0}

total = 0
grade_total = 0

for i in range(20):
    sub, t, g = input().split()
    t = float(t)
    if g in grade:
        total += t*grade[g]
        grade_total += t
    
print(round(total/grade_total,6))
    