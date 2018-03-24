# Uses python3
import sys


def optimal_weight(W, w):
    """Solve discrete Knapsack problem without repetition."""
    items_size = len(w) + 1
    weight_size = W + 1
    # pad first column with zeros
    table = [[0 for i in range(weight_size)] for j in range(items_size)]
    for i in range(1, items_size):
        for j in range(1, weight_size):
            table[i][j] = table[i - 1][j]
            ith_value = w[i - 1]
            if ith_value <= j:
                value = table[i - 1][j - ith_value] + ith_value
                if table[i][j] < value:
                    table[i][j] = value
    return table[items_size - 1][W]


if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
