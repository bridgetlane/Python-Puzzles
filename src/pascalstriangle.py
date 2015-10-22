lines = {0:[1], 1:[1,1]}

# returns the desired line of pascal's triangle (indexing starts at 0)
def pascal_line(line_num):
    completed_line = [1]
    if line_num in lines:
        completed_line = lines[line_num]
    else:
        index = 0
        while (index < line_num):
            completed_line.append(int((completed_line[index] * (line_num-index)) / (index + 1)))
            index += 1
        lines[line_num] = completed_line

    return completed_line
    
# simple printing function
def str_line(line):
    string = ""
    for i in line:
        string += str(i) + " "
    string += "\n"
    return string

# some examples of use
def main():
    line0 = pascal_line(0)
    line1 = pascal_line(1)
    line2 = pascal_line(2)
    line3 = pascal_line(3)
    line4 = pascal_line(4)
    line5 = pascal_line(5)
    
    print(str_line(line0))
    print(str_line(line1))
    print(str_line(line2))
    print(str_line(line3))
    print(str_line(line4))
    print(str_line(line5))

main()