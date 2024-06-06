#File Splitting:
#Develop a Python Function that reads a large text file (input.txt) and splits it
#into smaller files, each containing a specified number of lines. Function parameter
#is the number of lines per file. Generate multiple output files (output1.txt,
#output2.txt, etc.).


def split_file(input_file, lines_per_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    num_files = len(lines) // lines_per_file
    if len(lines) % lines_per_file != 0:
        num_files += 1

    for i in range(num_files):
        output_file = f'output{i + 1}.txt'
        with open(output_file, 'w') as file:
            start_index = i * lines_per_file
            end_index = start_index + lines_per_file
            file.writelines(lines[start_index:end_index])


print(split_file("lesson14_4_input.txt", 9))








