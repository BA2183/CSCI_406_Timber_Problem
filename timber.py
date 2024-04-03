import numpy as np
import time
import matplotlib.pyplot as plt
plt.style.use("Solarize_Light2")

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
        # random timber generators
        curr_arr = np.random.randint(1, 1001, size=i)
        # timer
        start_time = time.time()
        timber(curr_arr, 0, i-1)
        end_time = time.time()
        time_diff = end_time - start_time
        # record
        time_arr.append(time_diff)
        iter_arr.append(i)

    return time_arr, iter_arr

time_arr, iter_arr = perform_test(20)
# plot
plt.plot(iter_arr, time_arr)
plt.xticks(iter_arr)
plt.xlabel("timber length")
plt.ylabel("time (seconds)")
plt.title("Timber() performance based on timber length")
plt.show()
