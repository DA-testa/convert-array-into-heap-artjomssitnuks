# python3


def build_heap(data):
    swaps = []
    n = len(data)
    for i in range(n // 2 - 1, -1, -1):
        min_child_idx = 2 * i + 1
        while min_child_idx < n:
            if min_child_idx + 1 < n and data[min_child_idx + 1] < data[min_child_idx]:
                min_child_idx += 1
            if data[i] <= data[min_child_idx]:
                break
            swaps.append((i, min_child_idx))
            data[i], data[min_child_idx] = data[min_child_idx], data[i]
            i = min_child_idx
            min_child_idx = 2 * i + 1
    return swaps



def main():
    first_input = input()
    if first_input.startswith("I"):
        second_input = input()
        n = int(second_input)
        data = list(map(int, input().split()))
        assert len(data) == n
    elif first_input.startswith("F"):
        filename = str(input())
        filename = "tests/" + filename
        with open(filename, 'r') as f:
            n = int(f.readline())
            data = [int(x) for x in f.readline().split()]
    else:
        raise ValueError("Invalid input option")
    swaps = build_heap(data)
    print(len(swaps))
    for i, j in swaps:
        print(i, j)

if __name__ == '__main__':
    main()
