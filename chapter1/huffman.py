from collections import Counter
from heapq import heapify,heappop,heappush

def huffman_coding(message):
    freq = Counter(message)
    print(freq)
    min_head = [[cnt,[ch,''] ] for (ch,cnt) in freq.items()]
    print(min_head)
    heapify(min_head)
    print(min_head)
    while len(min_head) > 1:
        low1 = heappop(min_head)
        low2 = heappop(min_head)
        for pair in low1[1:]:
            pair[1] += '0'
        for pair in low2[1:]:
            pair[1] += '1'
        print("low",[low1[0] + low2[0]] + low1[1:] + low2[1:])
        heappush(min_head, [low1[0] + low2[0]] + low1[1:] + low2[1:])
        vocabulary = {pair[0]: pair[1] for pair in min_head[0][1:]}  # text -> code
        return vocabulary

sentence = 'this is an example for huffman encoding'
print(huffman_coding(sentence))

