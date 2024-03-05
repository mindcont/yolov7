import os

# xmlfilepath = r'../VOCData/VOCTrainVal/Annotations/'  # xml文件的路径
# saveBasePath = r'../VOCData/VOCTrainVal/ImageSets/'  # 生成的txt文件的保存路径
#
# trainval_percent = 0.8  # 训练验证集占整个数据集的比重（划分训练集和测试验证集）
# train_percent = 0.8  # 训练集占整个训练验证集的比重（划分训练集和验证集）
# total_xml = os.listdir(xmlfilepath)
# num = len(total_xml)
# list = range(num)
# tv = int(num * trainval_percent)
# tr = int(tv * train_percent)
# trainval = random.sample(list, tv)
# train = random.sample(trainval, tr)
#
# print("train and val size", tv)
# print("traub suze", tr)
train_path = r"D:\yolov7\datasets\weld\images\train"
test_path = r"D:\yolov7\datasets\weld\images\val"

train_images = os.listdir(train_path)
test_images = os.listdir(test_path)

ftrainval = open('train_list.txt', 'w')
ftest = open('val_list.txt', 'w')

for i in range(len(train_images)):
    name = "datasets/weld/images/train/" + train_images[i] + '\n'
    ftrainval.write(name)
ftrainval.close()

for i in range(len(test_images)):
    name = "datasets/weld/images/val/" + test_images[i] + '\n'
    ftest.write(name)
ftest.close()
