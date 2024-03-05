import os
import shutil

# 目录 A
dir_a = r'D:\yolov7\datasets\weld\images\train'

# 目录 B
dir_b = r'D:\yolov7\datasets\weld\labels\train'

# 获取目录 A 中的文件名列表
png_files = os.listdir(dir_a)

# 获取目录 B 中的文件名列表
txt_files = os.listdir(dir_b)

# 比较两个列表中的文件名，获取在目录 A 中存在但在目录 B 中不存在的文件名
diff_files = [filename for filename in png_files if filename[:-4] + '.txt' not in txt_files]

#判断差异目录是否存在
if not os.path.exists("diff"):
    os.mkdir("diff")
# 打印不同的文件名
for filename in diff_files:
    print(filename)

    #移动差异文件
    # source_file = os.path.join(dir_a, filename)
    # target_file = os.path.join("diff", filename)
    #
    # # 将文件移动到目标目录
    # shutil.copy2(source_file, target_file)

