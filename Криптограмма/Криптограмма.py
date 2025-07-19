def solution(n: int, m: int) -> int:
    if n == 0:
        return 1
    low, high = 0, m
    while low < high:
        mid = (low + high) // 2
        if S(n, mid) >= m:
            high = mid
        else:
            low = mid + 1
    return low

def S(n, L):
    if n == 0:
        return 1 if L >= 1 else 0
    if L == 0:
        return 0
        
    a_min = n + 1
    cur = 1
    if cur >= L:
        a_min = 0
    else:
        for i in range(1, min(n, 100) + 1):
            next_approx = cur * (n - i + 1) / i
            if next_approx > 10**18:
                a_min = i
                break
            if next_approx >= L:
                a_min = i
                break
            cur = cur * (n - i + 1) // i
            if cur >= L:
                a_min = i
                break
        else:
            a_min = n + 1
                
    if a_min == n + 1:
        return 10**18
        
    if a_min == 0:
        tail_sum = 0
    else:
        total_tail = 0
        c_val = 1
        total_tail += c_val
        for j in range(1, a_min):
            c_val = c_val * (n - j + 1) // j
            total_tail += c_val
        tail_sum = 2 * total_tail
        
    mid_length = n - 2 * a_min + 1
    if mid_length < 0:
        mid_length = 0
        
    return tail_sum + mid_length * L
