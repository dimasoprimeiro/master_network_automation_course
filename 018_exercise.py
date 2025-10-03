with open('file.txt') as f:
    content_list = f.readlines()

tmp_list = [line for line in content_list if line.strip() != '']
print(tmp_list)

with open('file_without_blanks.txt', 'w') as f:
    f.write(''.join(tmp_list))