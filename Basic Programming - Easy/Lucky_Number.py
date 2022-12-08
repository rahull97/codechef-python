def solve():
    number = int(input())

    if number % 2 == 1:
        return 1
    else:
        count_of_2 = 0
        while True:
            if number % 2 == 0:
                count_of_2 = count_of_2 + 1
                number = number // 2
            else:
                break
        if count_of_2 % 2 == 0:
            return 1
        else:
            return 0


def main():
    number_of_test_cases = int(input())
    for _ in range(number_of_test_cases):
        print(solve())


if __name__ == "__main__":
    main()
