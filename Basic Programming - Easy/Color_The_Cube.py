def solve():
    input_data = input().split()
    n, x1, x2, x3, x4, x5, x6 = list(map(int, input_data))

    if n % 2 == 1:
        n = n + 1

    total_litres = n//2

    total_cost = (x1 + x2 + x3 + x4 + x5 + x6) * total_litres

    return total_cost


def main():
    number_of_test_cases = int(input())
    for _ in range(number_of_test_cases):
        print(solve())


if __name__ == "__main__":
    main()
