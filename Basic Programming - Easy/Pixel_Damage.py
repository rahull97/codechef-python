def solve():
    h, w, x, y, k = list(map(lambda x: int(x), input().split()))
    d1 = w - x
    d2 = h - y
    d_sq = (d1 * d1 )+ (d2 * d2)
    k_sq = k * k
    if d_sq < k_sq:
        return 1
    return 0


def main():
    number_of_test_cases = int(input())
    for _ in range(number_of_test_cases):
        print(solve())


if __name__ == "__main__":
    main()
