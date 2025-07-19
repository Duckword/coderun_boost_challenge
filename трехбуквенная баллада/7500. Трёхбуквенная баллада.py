import string
def solve(ballad: str, n: int) -> int:
    alphabet_list = [0 for _ in range(26)]
    prefix_symbols_sum=[]
    for symbol in ballad:
        if symbol==' ':
            prefix_symbols_sum.append(alphabet_list.copy())
            continue
        alphabet_list[ ord(symbol) - ord('a')]+=1
        prefix_symbols_sum.append(alphabet_list.copy())

    count=0
    for i in range(1,n-1):
        if ballad[i]==' ' :
            continue

        for symbol_ind in range(26):
            add=prefix_symbols_sum[i-1][symbol_ind]*(prefix_symbols_sum[-1][symbol_ind]-prefix_symbols_sum[i][symbol_ind])
            count+=add


    return count



