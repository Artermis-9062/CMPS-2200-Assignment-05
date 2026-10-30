import math, queue
from collections import Counter

####### Problem 1 #######

class TreeNode(object):
    # we assume data is a tuple (frequency, character)
    def __init__(self, left=None, right=None, data=None):
        self.left = left
        self.right = right
        self.data = data
    def __lt__(self, other):
        return(self.data < other.data)
    def children(self):
        return((self.left, self.right))
    
def get_frequencies(fname):
    f=open(fname, 'r')
    C = Counter()
    for l in f.readlines():
        C.update(Counter(l))
    return C

# given a dictionary f mapping characters to frequencies, 
# create a prefix code tree using Huffman's algorithm
def make_huffman_tree(f):
    p = queue.PriorityQueue()
    # construct heap from frequencies, the initial items should be
    # the leaves of the final tree
    for c in f.keys():
        p.put(TreeNode(None,None,(f[c], c)))

    # greedily remove the two nodes x and y with lowest frequency,
    # create a new node z with x and y as children,
    # insert z into the priority queue (using an empty character "")
    while (p.qsize() > 1):
        # TODO
        pass
        
    # return root of the tree
    return p.get()

# Perform a traversal on the prefix code tree to collect all encodings.
# Recursively call get_code, appending 0 or 1 to prefix as appropriate
# depending on if the call is to the left or right child.
# When a leaf is found, update the code dict object to map from
# the value in the leaf to the encoding specified by prefix.
# Return the code object.
def get_code(node, prefix="", code={}):
    # TODO - perform a tree traversal and collect encodings for leaves in code
    pass

# Given an alphabet and frequencies, compute the cost of a fixed length encoding.
# You'll have to consider the total number of unique elements in f to 
# determine the number of bits needed to represent each character.
def fixed_length_cost(f):
    # TODO
    pass

# given a Huffman encoding and character frequencies, compute cost of a Huffman encoding
def huffman_cost(C, f):
    # TODO
    pass

def analyze_files():
    for fname in ['alice29.txt', 'asyoulik.txt', 'f1.txt', 'fields.c', 'grammar.lsp']:
        f = get_frequencies(fname)
        print("Fixed-length cost:  %d" % fixed_length_cost(f))
        T = make_huffman_tree(f)
        C = get_code(T)
        print("Huffman cost:  %d" % huffman_cost(C, f))


####### Problem 4 #######

test_cases = [('book', 'back'), ('kookaburra', 'kookybird'), ('relevant', 'elephant')]
alignments = [('book', 'back'), ('kookaburra', 'kookybird-'), ('relev-ant','-elephant')]

def MED(S, T):
    # TODO - modify to account for insertions, deletions and substitutions
    if (S == ""):
        return(len(T))
    elif (T == ""):
        return(len(S))
    else:
        if (S[0] == T[0]):
            return(MED(S[1:], T[1:]))
        else:
            return(1 + min(MED(S, T[1:]), MED(S[1:], T)))


def fast_MED(S, T):
    # TODO -  implement bottom-up memoization
    # returns only the edit distance cost
    pass

def fast_align_MED(S, T):
    # TODO - implement bottom-up memoization, allowing
    # for traceback of alignment
    # returns the two alignments (see test_align)
    pass