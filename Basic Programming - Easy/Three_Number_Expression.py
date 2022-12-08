def solve():
    a, b, c = input().split()
    a, b, c = int(a), int(b), int(c)

    li = [a, b, c]
    li.sort()

    if li[2] == li[0] + li[1]:
        return "YES"
      
    return "NO"


def main():
    number_of_test_cases = int(input())
    for _ in range(number_of_test_cases):
        print(solve())


if __name__ == "__main__":
    main()
