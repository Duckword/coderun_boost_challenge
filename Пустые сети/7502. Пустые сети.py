
def solve(a: int, k: int, n: int) -> int:
    MOD = 10 ** 9 + 7

    total = k + n
    m = min(k, n)
    num = 1
    for i in range(m):
        num = (num * (total - i)) % MOD

    denom = 1
    for i in range(1, m + 1):
        denom = (denom * i) % MOD

    binom = num * pow(denom, MOD - 2, MOD) % MOD

    return pow(binom, MOD - 2, MOD)

