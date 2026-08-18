# Matrix Chain Multiplication using Dynamic Programming

def matrix_chain_order(p):
    n = len(p) - 1

    # dp[i][j] = minimum multiplication cost
    dp = [[0 for _ in range(n)] for _ in range(n)]

    # split[i][j] stores the best split position
    split = [[0 for _ in range(n)] for _ in range(n)]

    # Chain length
    for length in range(2, n + 1):

        for i in range(n - length + 1):

            j = i + length - 1

            dp[i][j] = float('inf')

            for k in range(i, j):

                cost = (
                    dp[i][k]
                    + dp[k + 1][j]
                    + p[i] * p[k + 1] * p[j + 1]
                )

                if cost < dp[i][j]:
                    dp[i][j] = cost
                    split[i][j] = k

    return dp, split


# Construct optimal parenthesization
def print_optimal_order(split, i, j):

    if i == j:
        return f"A{i + 1}"

    k = split[i][j]

    left = print_optimal_order(split, i, k)
    right = print_optimal_order(split, k + 1, j)

    return f"({left} × {right})"


# Matrix dimensions
# A1 = 10x30
# A2 = 30x5
# A3 = 5x60
# A4 = 60x10

p = [10, 30, 5, 60, 10]

dp, split = matrix_chain_order(p)

n = len(p) - 1

optimal_cost = dp[0][n - 1]

optimal_order = print_optimal_order(
    split, 0, n - 1
)


print("=" * 55)
print("MATRIX CHAIN MULTIPLICATION")
print("=" * 55)

print("\nMatrices:")
print("A1 = 10 x 30")
print("A2 = 30 x 5")
print("A3 = 5 x 60")
print("A4 = 60 x 10")

print("\nMinimum Number of Scalar Multiplications:")
print(optimal_cost)

print("\nOptimal Multiplication Order:")
print(optimal_order)

print("\nDP Cost Table:")
print("-" * 55)

for row in dp:
    print(row)
