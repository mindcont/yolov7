import os

def process_txt_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    modified_lines = []
    for line in lines:
        split_data = line.strip().split(' ')
        if len(split_data) > 5:
            modified_line = ' '.join(split_data[:5]) + '\n'
            modified_lines.append(modified_line)
        else:
            modified_lines.append(line)

    with open(file_path, 'w') as file:
        file.writelines(modified_lines)

# 源目录
source_dir = r'D:\yolov7\runs\detect\exp\labels'

# 遍历源目录下的所有 .txt 文件
for filename in os.listdir(source_dir):
    if filename.endswith('.txt'):
        file_path = os.path.join(source_dir, filename)
        process_txt_file(file_path)