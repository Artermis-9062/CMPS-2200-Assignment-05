# CMPS 2200 Assignment 5
## Answers

**Name:** Chuong Hoang Pham
_________________________

Place all written answers from `assignment-05.md` here for easier grading.


**1: Fixed-Length vs. Variable-Length Codes**

- **1d. (5 pts)** What trend do you see?

| File | Fixed-length cost | Huffman cost | Huffman / Fixed |
|---|---|---|---|
| alice29.txt | 919071.34 | 676374 | 0.736 |
| asyoulik.txt | 762022.51 | 606448 | 0.796 |
| f1.txt | 1244.55 | 826 | 0.664 |
| fields.c | 72384.16 | 56206 | 0.776 |
| grammar.lsp | 23248.54 | 17356 | 0.747 |

Huffman is consistently cheaper, using about $66\%$–$80\%$ of the fixed-length
cost, because character frequencies in real text are highly skewed.

- **1e. (4 pts)** What is the expected
  cost of a Huffman encoding for the document? Is it consistent across
  documents?

With equal frequencies the Huffman tree is balanced, so every code has length
about $\log_2 |\Sigma|$ and the cost is about $n \log_2 |\Sigma|$ for a document of
$n$ characters, the same as fixed-length. It depends only on $n$ and $|\Sigma|$,
so it is consistent across such documents.


**2: Making Change**

- **2a. (5 pts)** Given a $N$ dollars, state a greedy algorithm for producing
as few coins as possible that sum to $N$.

Repeatedly take the largest coin $2^i \le N$ and set $N \leftarrow N - 2^i$
until $N = 0$.

- **2b. (5 pts)** Prove that this algorithm is optimal by proving the greedy
  choice and optimal substructure properties.

**Greedy choice property:** Let $2^i$ be the largest coin with $2^i \le N$. We show
some optimal solution contains a coin of value $2^i$.

Take any optimal solution $O$ for $N$. If it contains $2^i$, we are done.
Otherwise, every coin in $O$ is smaller than $2^i$ (coins larger than $2^i$ would
exceed $N$), so each coin is one of $2^0, 2^1, \dots, 2^{i-1}$, and they sum to
$N \ge 2^i$.

Sort the coins of $O$ from smallest to largest and add them up one at a time.
Each coin is a power of 2 that divides $2^i$, and each running sum is a multiple
of the next (larger or equal) coin. So the running sum can never jump over $2^i$:
it must land on exactly $2^i$ for some group of coins $G \subseteq O$. Since every
coin is smaller than $2^i$, $G$ has at least 2 coins.

Replace $G$ with a single coin of value $2^i$. The total is still $N$, but we use
at least one fewer coin. This contradicts the optimality of $O$, so every optimal
solution must contain $2^i$.

**Optimal substructure property:** Let $O$ be an optimal solution for $N$ that
contains $2^i$. Then $O' = O \setminus \{2^i\}$ is a solution for the subproblem
$N - 2^i$. We claim $O'$ is optimal for it. Suppose instead there is a solution
$S'$ for $N - 2^i$ with fewer coins than $O'$. Then $S' \cup \{2^i\}$ is a
solution for $N$ with fewer coins than $O$, contradicting that $O$ is optimal.

**Conclusion:** By greedy choice, taking the largest coin $2^i$ is safe. By
optimal substructure, we then only need an optimal solution for $N - 2^i$, which
the algorithm finds by repeating the same step. So the algorithm is optimal.

- **2c. (4 pts)** What is the work and span of your algorithm?

Using $\lfloor \log_2 N \rfloor + 1$ denominations, the algorithm takes
$O(\log N)$ steps, each depending on the previous one. Work $= O(\log N)$ and
span $= O(\log N)$.
