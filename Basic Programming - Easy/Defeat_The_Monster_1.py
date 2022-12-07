def solve():
    h, x, y = input().split()
    h, x, y = int(h), int(x), int(y)

    i = h + y - x
    m = i + y - x

    if m < i:
        return 1
    else:
        return 0 


def main():
    n = int(input())
    for _ in range(n):
        print(solve())


if __name__ == "__main__":
    main()
