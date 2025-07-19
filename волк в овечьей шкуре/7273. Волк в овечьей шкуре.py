from typing import List
def solution(n: int, a: List[int]) -> int:
    if n==1:
        return 0
    l=0
    r=0
    count=0
    max_count=0
    dict_of_elems={}
    while r<n:
        if len(dict_of_elems) <= 1:
            dict_of_elems[a[r]] = 1 + dict_of_elems.get(a[r],0)
            r += 1
            count += 1
        else:
            max_count=count
            r-=1
            break
    if len(dict_of_elems)==2:
        max_count=count
    diff=1
    while r<n:
        if diff==1:
            if r-l+1>max_count:
                max_count=r-l+1
            r+=1
            if r==n:
                break
            if dict_of_elems.get(a[r],0)==0:
                diff+=1
            dict_of_elems[a[r]] = 1 + dict_of_elems.get(a[r],0)
        else:
            dict_of_elems[a[l]]-=1
            if dict_of_elems[a[l]]==0:
                diff-=1
            l+=1
    return max_count

print(solution(20,list(range(20))))
print(solution(20,[0]*10+[1]*10))
print(solution(2,[1,1]))
print(solution(6,[3 ,3 ,1 ,2, 2 ,1]))






