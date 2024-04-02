def read_input():
    arr_length = int(input())
    in_arr = [item for item in map(int, input().split())]
    return arr_length, in_arr

def timber(in_arr, head, tail):
    # init memory
    mem = [[in_arr[row] if row == col else 0 for row in range(tail+1)] for col in range(tail+1)]
    # starting j
    start_j = 1
    while start_j < tail+1:
        # this work that i reset to 0 every time, go back to the top row
        # while j only restart where j where originally with one step a head
        j = start_j
        i = 0
        while i < tail+1 and j < tail+1:
            # relation
            if i != j and i < j:
                mem[i][j] = sum(in_arr[i:j+1]) - min(mem[i+1][j], mem[i][j-1])
            # move both j and i
            j += 1
            i += 1
        # move the next diagonal rows on the next columns
        start_j += 1
        # return result from desired input
    return mem[head][tail]

length, arr = read_input()
print(timber(arr, 0, length))
