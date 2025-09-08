
def main():
    g = int(input())
    li = [i for i in range(1,(g//2)+2)]
    s, e = 0, (g//2)
    isFin = False

    while s < g//2:
        sum = (li[s] + li[e])*(li[e] - li[s])
        #print(sum, s, e)
        if sum == g:
            isFin = True
            print(li[e])
            e += 1
            s += 1
        elif sum > g:
            e -= 1
        elif sum < g:
            e += 1
            s += 1
        
    if isFin == False:
        print("-1")
main()