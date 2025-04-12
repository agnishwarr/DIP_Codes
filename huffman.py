import heapq
from collections import defaultdict, Counter
class Node:
    def __init__(self, symbol=None, freq=None):
        self.symbol = symbol
        self.freq = freq
        self.left = None
        self.right = None
    def __lt__(self, other):
        return self.freq < other.freq
def build_huffman_tree(data):
    frequency = Counter(data)
    heap = [Node(symbol, freq) for symbol, freq in frequency.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(freq=left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)
    return heap[0]
def build_huffman_table(root):
    huffman_table = {}

    def _build_huffman_table(node, code):
        if node is not None:
            if node.symbol is not None:
                huffman_table[node.symbol] = code
            _build_huffman_table(node.left, code + '0')
            _build_huffman_table(node.right, code + '1')
    _build_huffman_table(root, '')
    return huffman_table
def huffman_encode(data):
    root = build_huffman_tree(data)
    huffman_table = build_huffman_table(root)
    encoded_data = ''.join(huffman_table[symbol] for symbol in data)
    return encoded_data, huffman_table
def huffman_decode(encoded_data, huffman_table):
    decoded_data = ''
    symbol = ''
    for bit in encoded_data:
        symbol += bit
        if symbol in huffman_table:
            decoded_data += huffman_table[symbol]
            symbol = ''
    return decoded_data
image_data = "ABBCCCDDDDEEEEE"
encoded_data, huffman_table = huffman_encode(image_data)
print("Encoded data:", encoded_data)
print("Huffman table:", huffman_table)
decoded_data = huffman_decode(encoded_data, huffman_table)
print("Decoded data:", decoded_data)
