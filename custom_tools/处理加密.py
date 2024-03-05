import os
import shutil

# 源目录
source_dir = r'D:\yolov7\runs\detect\exp\labels'

# 目标目录
target_dir = r'D:\train_data'

# 确保目标目录存在
os.makedirs(target_dir, exist_ok=True)

# 遍历源目录中的所有 .txt 文件
for filename in os.listdir(source_dir):
    if filename.endswith('.txt'):
        # 构造源文件路径和目标文件路径
        source_file = os.path.join(source_dir, filename)
        target_file = os.path.join(target_dir, filename[:-4] + '.dump')

        # 复制并重命名文件
        shutil.copy2(source_file, target_file)
        print("正在处理",source_file,target_file)