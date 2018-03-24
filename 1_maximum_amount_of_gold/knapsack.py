# Uses python3
import sys

def optimal_weight(W, w):
    """Solve discrete Knapsack problem without repetition."""
    table = {}
    items_size = len(w) + 1
    weight_size = W + 1
    # pad first column with zeros
    for i in range(items_size):
        table[0, i] = 0
    # pad first row with zeros
    for i in range(weight_size):
        table[i, 0] = 0
    for i in range(1, items_size):
        for j in range(1, weight_size):
            table[j, i] = table[j, i - 1]
            ith_value = w[i - 1]
            if ith_value <= j:
                value = table[j - ith_value, i - 1] + ith_value
                if table[j, i] < value:
                    table[j, i] = value
    return table[W, items_size - 1]


if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
