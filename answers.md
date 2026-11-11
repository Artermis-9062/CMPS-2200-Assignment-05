# CMPS 2200 Assignment 5
## Answers

**Name:** Chuong Hoang Pham
_________________________

Place all written answers from `assignment-05.md` here for easier grading.


**1: Fixed-Length vs. Variable-Length Codes**

- **1d. (5 pts)** What trend do you see?

| File | Fixed-length cost | Huffman cost | Huffman / Fixed |
|---|---|---|---|
| alice29.txt | 1039367 | 676374 | 0.651 |
| asyoulik.txt | 876253 | 606448 | 0.692 |
| f1.txt | 1340 | 826 | 0.616 |
| fields.c | 78050 | 56206 | 0.720 |
| grammar.lsp | 26047 | 17356 | 0.666 |

Huffman is consistently cheaper, using about $62\%$–$72\%$ of the fixed-length
cost (fixed-length uses $\lceil \log_2 |\Sigma| \rceil$ bits per character), because character frequencies in real text are highly skewed.

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

With denominations $2^0,\dots,2^k$, the algorithm uses $\lfloor N/2^k \rfloor$ coins
of the largest denomination, then at most one coin of each smaller denomination,
so it takes $O(N/2^k + k)$ steps, each depending on the previous one. When
$k \approx \log_2 N$ this is $O(\log N)$. Work $= O(N/2^k + k) = O(\log N)$ and
span $=$ work, since the steps are sequential.


**3: Edit Distance**

- **3a.** State the optimal substructure property for edit distance with
  insertions, deletions and substitutions of unit cost.

Compare the first characters of $S$ and $T$:

$$
MED(S,T)=\begin{cases}
|T| & \text{if } S=\text{""} \\
|S| & \text{if } T=\text{""} \\
MED(S[1:],T[1:]) & \text{if } S[0]=T[0] \\
1+\min\big(MED(S,T[1:]),\ MED(S[1:],T),\ MED(S[1:],T[1:])\big) & \text{otherwise}
\end{cases}
$$

The three terms in the $\min$ are: insert $T[0]$ (leaves $S$ vs. $T[1:]$), delete
$S[0]$ (leaves $S[1:]$ vs. $T$), and substitute $S[0]$ with $T[0]$ (leaves
$S[1:]$ vs. $T[1:]$).
