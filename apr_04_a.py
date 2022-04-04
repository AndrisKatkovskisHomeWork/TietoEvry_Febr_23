from pathlib import Path

def file_line_len(fpath):
    count_lines = 0
    not_empty_lines = 0
    to_find = "\n"
    with open(fpath, encoding="utf-8") as my_file:
        for line in my_file:
            if to_find in line:
                count_lines += 1
                if len(line.strip()) > 0:
                    not_empty_lines += 1
    return count_lines, not_empty_lines

my_file = Path("veidenbaums.txt")
print(my_file)
print(file_line_len(my_file))
