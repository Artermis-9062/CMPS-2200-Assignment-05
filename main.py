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
    def __repr__(self):
        return f"{(self.left, self.right, self.data)}"
    
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
        # First two element in the queue is 2 nodes we looking for
        first_node = p.get()
        second_node = p.get()
        new_node = TreeNode(first_node, second_node, (first_node.data[0] + second_node.data[0], '')) # .data()[0] should be the freq of the node.         
        p.put(new_node)
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
    if node.left == None and node.right == None:
        code[node.data[1]] = prefix
        return code
    #Choose left
    if node.left:
        get_code(node.left, prefix + "0", code)
    if node.right:
        get_code(node.right, prefix + "1", code)
    return code
    pass

# Given an alphabet and frequencies, compute the cost of a fixed length encoding.
# You'll have to consider the total number of unique elements in f to 
# determine the number of bits needed to represent each character.
def fixed_length_cost(f):
    # TODO
    bits_per_char = math.log2(len(f.keys()))
    num_char = sum(f.values())
    return bits_per_char * num_char
    pass

# given a Huffman encoding and character frequencies, compute cost of a Huffman encoding
def huffman_cost(C, f):
    # TODO
    return sum(len(C[i]) * f[i] for i in C.keys())
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