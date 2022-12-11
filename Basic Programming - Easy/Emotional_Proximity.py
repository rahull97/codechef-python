def solve():
    p, x, y, z = list(map(lambda x: int(x), input().split()))

    if z == 1:
        final_emotional_proximity = p * ((100 + y)/100)
    else:
        final_emotional_proximity = p * ((100 - x)/100)
    return final_emotional_proximity


def main():
    number_of_test_cases = int(input())
    for _ in range(number_of_test_cases):
        print(solve())


if __name__ == "__main__":
    main()
