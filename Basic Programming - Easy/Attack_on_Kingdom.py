def solve():
    no_of_days = int(input())
    temperatures = list(map(int, input().split()))
    temperatures.sort()
    if len(temperatures) > 1:
        return temperatures[1]
    else:
        return temperatures[0]


def main():
    number_of_test_cases = int(input())
    for _ in range(number_of_test_cases):
        print(solve())


if __name__ == "__main__":
    main()
