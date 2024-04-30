def read_input():
    arr_length = int(input())
    in_arr = [item for item in map(int, input().split())]
    return arr_length, in_arr

# calculate the segment sum to reduce sum calculation
def segment_sum(in_arr, length):
    # empty table
    sum_arr = [[0 for _ in range(length+1)] for _ in range(length+1)]
    for i in range(length):
        sum_arr[i][i] = in_arr[i]
        for j in range(i+1, length):
            sum_arr[i][j] = sum_arr[i][j - 1] + in_arr[j]

    return sum_arr
def timber(in_arr, sum_arr, length):
    # init memory
    mem = [[(in_arr[row], 'S') if row == col else (0, ' ') for row in range(length)] for col in range(length)]
    # starting j
    start_j = 1
    while start_j < length:
        # this work that i reset to 0 every time, go back to the top row
        # while j only restart where j where originally with one step a head
        j = start_j
        i = 0
        while i < length and j < length:
            # relation
            if i != j and i < j:
                if mem[i+1][j][0] <= mem[i][j-1][0]:
                    mem[i][j] = (sum_arr[i][j] - mem[i+1][j][0], 'L')
                elif mem[i][j-1][0] < mem[i+1][j][0]:
                    mem[i][j] = (sum_arr[i][j] - mem[i][j-1][0], 'R')
            # move both j and i
            j += 1
            i += 1
        # move the next diagonal rows on the next columns
        start_j += 1
        # return result from desired input
    return mem

def process_traceback(length, p):
    steps = [str(i) for i in range(1, length+1)]
    result = []
    i = 0
    j = length-1
    while j >= i:
        # move down
        if p[i][j][1] == 'L':
            result.append(steps[0])
            steps = steps[1:]
            i += 1
        # move up
        elif p[i][j][1] == 'R':
            result.append(steps[-1])
            steps = steps[:-1]
            j -= 1
        # base case
        else:
            result.append(steps[-1])
            i += 1
    return ' '.join(result)
    
length, arr = read_input()
sum_table = segment_sum(arr, length)
output_matrix = timber(arr, sum_table, length)
result = output_matrix[0][length-1][0]
traceback = process_traceback(length, output_matrix)
print(result)
print(traceback)

    

