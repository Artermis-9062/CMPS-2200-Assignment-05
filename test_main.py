from main import *

# 10 pts
def test_huffman_simple():
    """ example from class """
    f = Counter(["A", "A", "A", "A", "A", "A", "A", "A", "A", "B", "C", "D"])
    T = make_huffman_tree(f)
    C = get_code(T)
    assert huffman_cost(C, f) == 17

# 6 pts
def test_MED():
    for S, T in test_cases:
        assert fast_MED(S, T) == MED(S, T)

# 6 pts                               
def test_align():
    for i in range(len(test_cases)):
        S, T = test_cases[i]
        align_S, align_T = fast_align_MED(S, T)
        assert (align_S == alignments[i][0] and align_T == alignments[i][1])
