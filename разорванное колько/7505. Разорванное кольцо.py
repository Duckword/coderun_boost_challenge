import sys

class FastInput:
    def __init__(self):
        self.stdin = sys.stdin

    def read_line(self):
        return sys.stdin.readline().strip()

    def read_tokens(self):
        return self.read_line().split()

    def read_int(self):
        return int(self.read_line())

    def read_ints_a(self):
        list_res=list(map(int, self.read_tokens()))
        return [i-1 for i in list_res]

    def read_ints_b(self):
        return list(map(int, self.read_tokens()))


def min_change(n,a,b):
    summa=0
    count_parts=0
    for i in range(n):
        if a[i]<0:
            continue
        current=i
        min_ind=i
        while current!=-1:
            if b[current]<b[min_ind]:
                min_ind=current
            tmp=current
            current=a[current]
            a[tmp]=-1
        summa+=b[min_ind]
        count_parts+=1
    if count_parts>1:
        return summa
    else:
        return 0


# ввод/вывод
# не изменяйте сигнатуру метода
def solution():
    results=list()
    input_channel=FastInput()
    t=input_channel.read_int()
    for i in range(t):
        n=input_channel.read_int()
        a=input_channel.read_ints_a()
        b=input_channel.read_ints_b()
        res=min_change(n,a,b)
        results.append(res)
    for item in results:
        print(item)


