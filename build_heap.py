# python3


def build_heap(data):
    swaps = []
    n = len(data)
    for i in range(n // 2 - 1, -1, -1):
        while True:
            max_child_idx = 2 * i + 1
            if max_child_idx + 1 < n and data[max_child_idx + 1] > data[max_child_idx]:
                max_child_idx += 1
            if data[i] >= data[max_child_idx]:
                break
            swaps.append((i, max_child_idx))
            data[i], data[max_child_idx] = data[max_child_idx], data[i]
            i = max_child_idx
    return swaps

def main():
    input_opt, n = input().split()

    n = int(n)

    if input_opt == "I":
        data = list(map(int, input().split()))
        assert len(data) == n
    elif input_opt == "F":
        with open(input(), "r") as f:
            data = list(map(int, f.readline().split()))
        assert len(data) == n
    else:
        raise ValueError("Invalid input option")

    swaps = build_heap(data)
    assert len(swaps) < 4

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
