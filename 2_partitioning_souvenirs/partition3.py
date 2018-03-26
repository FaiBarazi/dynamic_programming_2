# Uses python3
import sys
import itertools


def partition3(A):
    """Check if  All items in A can be partitione to 3 buckets of equal value.
    return 1 or 0 if possible or not.
    """
    values_size = len(A) + 1
    total_value = sum(A)
    bucket_sum = total_value // 3
    bucket_sum += 1
    if len(A) < 3 or total_value % 3:
        return 0
    table = [[0 for i in range(values_size)] for i in range(bucket_sum)]
    for i in range(1, bucket_sum):
        for j in range(1, values_size):
            x = i - A[j - 1]
            if A[j - 1] == i or (x and table[x][j - 1]):
                if table[i][j - 1] == 0:
                    table[i][j] = 1
                else:
                    table[i][j] = 2
            else:
                table[i][j] = table[i][j - 1]
    if table[-1][-1] == 2:
        return 1
    else:
        return 0


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    print(partition3(A))
