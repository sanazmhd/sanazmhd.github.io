def binaryserach(lst,target):
    maxindex=len(lst)-1
    minindex=0
    resulttemp=[]
    while(maxindex>=minindex):
        mid = (maxindex + minindex) // 2
        if lst[mid]==target:
            resulttemp.append(mid)
            left=mid-1
            right=mid+1
            while(left>=0 and lst[left] == target ):
              resulttemp.append(left)
              left-=1
            while(right<len(lst) and lst[right]==target):
              resulttemp.append(right)
              right+=1
            if len(resulttemp)==1:
                return resulttemp[0]
            else:
                return resulttemp
        elif lst[mid]<target:
               minindex=mid+1
        else:
               maxindex=mid-1
    return -1