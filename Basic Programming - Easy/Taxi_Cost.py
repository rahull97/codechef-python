def solve():
    ans = 0
    n, x = list(map(int, input().split()))

    a = []

    for i in range(n):
        a.append(int(input()))

    for i, e in enumerate(a):
        if i == 0:
            if a[i] == 1:
                ans = ans + x
        else:
            if a[i] == 1 or a[i-1] == 1:
                ans = ans + x

    return ans


def main():
    number_of_test_cases = int(input())
    for _ in range(number_of_test_cases):
        print(solve())


if __name__ == "__main__":
    main()
