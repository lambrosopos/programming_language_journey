num = int(input())
stack = list(map(int,input().split())) 
if num == 1:
    print(0)
else:
    lis = [0] * num

    stack.reverse() 
    def bsearch(left,right,target,lis):
        while left < right:
            mid = (left+right)//2
            if lis[mid] < target :
                left = mid + 1
            else:
                right = mid
        return right
    
    lis[0] = stack[0]
    j = 0
    for i in range(1,num):
        if lis[j] < stack[i]:
            j += 1
            lis[j] = stack[i]
        else:
            idx = bsearch(0, j, stack[i], lis)
            lis[idx] = stack[i]

        print(lis)

    print(num-j-1)
