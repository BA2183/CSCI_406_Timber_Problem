import numpy as np
import time
import matplotlib.pyplot as plt
def read_input():
    arr_length = int(input())
    in_arr = [item for item in map(int, input().split())]
    return arr_length, in_arr

def timber(in_arr, head, tail):
    if head == tail:
        return in_arr[head]
    return sum(in_arr[head:tail+1]) - min(timber(in_arr, head+1, tail), timber(in_arr, head, tail-1))

def perform_test(n):
    iter_arr = []
    time_arr = []
    for i in range(1, n+1):
        curr_arr = np.random.randint(1, 1001, size=n)

        start_time = time.time()
        timber(curr_arr, 0, i-1)
        end_time = time.time()

        time_diff = end_time - start_time

        time_arr.append(time_diff)
        iter_arr.append(i)

    return time_arr, iter_arr

# length, timbers = read_input()
# print(f"input: {(length, timbers)}")
# timbers = np.array([5, 6, 9, 7])
# length = 4
# out = timber(timbers, 0, length-1)
# print(out)
time_arr, iter_arr = perform_test(20)
plt.plot(iter_arr, time_arr)
plt.show()