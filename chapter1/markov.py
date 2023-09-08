import numpy as np


def markov():
    init_array = np.array([0, 1, 0])
    transfer_matrix = np.array([[0.5, 0.2, 0.3],
                                [0.3, 0.1, 0.6],
                                [0.3, 0.6, 0.1]])
    rtmp = transfer_matrix
    for i in range(45):
        res = np.dot(rtmp, transfer_matrix)
        print(i+1, "\t", res)
        rtmp = res


markov()
