import random
def gen_max_test(n=200000):
    print(1)
    print(n)
    print(*(random.randint(1, 10**9) for _ in range(n)))
gen_max_test()
