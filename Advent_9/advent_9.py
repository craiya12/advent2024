import os
import pandas as pd
import numpy as np
import re
import copy

# Define the file path
file_path = "advent_9.txt"

# Open the file and read the content
with open(file_path, "r") as file:
    digit_string = file.read().strip()  # Read and remove any extra whitespaces/newlines

digit_list = []

file_content = 0

turn = "file_s"

for num in digit_string:
    if turn == "file_s" and num != "0":

        num_list = []

        for i in range(int(num)):
            num_list.append(str(file_content))
        digit_list.append(num_list)
        turn = "file_f"
        file_content += 1
    elif turn == "file_f" and num != "0":

        dot_list = []

        for j in range(int(num)):
            dot_list.append(".")
        digit_list.append(dot_list)
        turn = "file_s"

    else:
        if turn == "file_s":
            turn = "file_f"
        else:
            turn = "file_s"

# print(digit_list)

# print(''.join(digit_list))


progress_list = copy.deepcopy(digit_list)
backward = True
j = -1

while backward == True:

    i = 0

    forward = True
    #print('changing j:',j, progress_list[j])
    while forward == True:

        if len(progress_list) + j <= 0:
            backward = False
            break

        if i == len(progress_list) + j:
            break
        

        if (
            len(progress_list[j]) <= len(progress_list[i])
            and progress_list[i][0] == "."
            and progress_list[j][0] != "."
        ):

            # print(j, progress_list[j], len(progress_list[j]), len(progress_list[i]))
            final_list = []
            for k in progress_list:
                for l in k:
                    final_list.append(l)
            # print("".join(final_list))

            transfer_list = progress_list[j].copy()

            for m in range(len(progress_list[j])):
                progress_list[j][m] = "."

            progress_list.insert(i, transfer_list)

            for k in range(len(transfer_list)):
                progress_list[i + 1].remove(".")
            if len(progress_list[i+1])==0:
                del progress_list[i+1]

            # print(progress_list)

            forward = False
        elif i + 1 > len(progress_list):
            forward = False

        i += 1

    j = j - 1

# print(progress_list)

final_list = []
for k in progress_list:
    for l in k:
        final_list.append(l)


#print("".join(final_list))
#print(final_list)


total_sum=0

for i,item in enumerate(final_list):
    if item=='.':
        continue
    total_sum=total_sum+i*int(item)
        
#print(''.join(progress_list))
print(total_sum)

