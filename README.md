# Optimal Cost Computation in Matrix Chain Multiplication using DP Technique

## Overview

This project implements Matrix Chain Multiplication using the Dynamic Programming technique. The objective is to determine the optimal order of multiplying a chain of matrices so that the total number of scalar multiplications is minimized.

## Problem Statement

Given a chain of four matrices:

```text
A1 = 10 × 30
A2 = 30 × 5
A3 = 5 × 60
A4 = 60 × 10
```

Find the optimal order of multiplication using Dynamic Programming and determine the minimum number of scalar multiplications required.

## Objectives

* Implement Matrix Chain Multiplication using Dynamic Programming.
* Calculate the minimum multiplication cost.
* Determine the optimal parenthesization.
* Construct the DP cost table.
* Analyze the time and space complexity.

## Dynamic Programming Formula

For matrices `Ai ... Aj`, the minimum cost is:

```text
m[i][j] = min {
    m[i][k] + m[k+1][j]
    + p[i-1] × p[k] × p[j]
}
```

where:

```text
i ≤ k < j
```

## Matrix Dimensions

| Matrix | Dimension |
| ------ | --------- |
| A1     | 10 × 30   |
| A2     | 30 × 5    |
| A3     | 5 × 60    |
| A4     | 60 × 10   |

The dimension array is:

```text
P = [10, 30, 5, 60, 10]
```

## Optimal Order

The optimal multiplication order is:

```text
((A1 × A2) × (A3 × A4))
```

### Cost Calculation

First multiply `A1 × A2`:

```text
10 × 30 × 5 = 1500
```

Then multiply `A3 × A4`:

```text
5 × 60 × 10 = 3000
```

Finally multiply the resulting matrices:

```text
10 × 5 × 10 = 500
```

Therefore:

```text
Total Cost = 1500 + 3000 + 500
           = 5000
```

### Final Result

**Minimum number of scalar multiplications = 5000**

## Complexity Analysis

| Complexity       | Value |
| ---------------- | ----- |
| Time Complexity  | O(n³) |
| Space Complexity | O(n²) |

The DP approach requires `O(n³)` time because every possible chain length and split position is evaluated. The DP table requires `O(n²)` space.

## Sample Output

```text
MATRIX CHAIN MULTIPLICATION

Matrices:
A1 = 10 x 30
A2 = 30 x 5
A3 = 5 x 60
A4 = 60 x 10

Minimum Number of Scalar Multiplications:
5000

Optimal Multiplication Order:
((A1 × A2) × (A3 × A4))
```

## Project Structure

```text
Matrix-Chain-Multiplication/
│
├── matrix_chain_multiplication.py
├── index.html
└── README.md
```

## Applications

* Compiler Optimization
* Database Query Optimization
* Scientific Computing
* Computer Graphics
* Numerical Computation
* Optimization Problems

## Conclusion

The Matrix Chain Multiplication problem demonstrates the effectiveness of Dynamic Programming in optimizing the order of matrix operations. For the given four matrices, the optimal parenthesization is `((A1 × A2) × (A3 × A4))`, requiring only **5000 scalar multiplications**.

## Technologies Used

* Python 3
* Dynamic Programming
* Recursion
* Algorithm Analysis

## Author

**Akash N**

B.E. Computer Science and Engineering (AI)
Chennai Institute of Technology
