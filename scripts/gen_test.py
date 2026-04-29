import random

def generate_test(n, m):
    print(1) # Number of test cases
    print(f"{n} {m}")
    a = [random.randint(1, m) for _ in range(n)]
    print(*(a))

if __name__ == "__main__":
    # Generate a large test case
    generate_test(10**5, 10**5)
