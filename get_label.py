import os
# 该脚本用于生成数据集的标签文件label.txt，文件内容格式如下：

def assign_category_number(folder_name):
    if "其他垃圾" in folder_name:
        return 0
    elif "厨余垃圾" in folder_name:
        return 1
    elif "可回收物" in folder_name:
        return 2
    elif "有害垃圾" in folder_name:
        return 3
    elif "学术垃圾" in folder_name:
        return 4
    else:
        return -1  # 如果文件夹名不符合上述分类，返回-1表示未分类


def main(directory_path):
    # 获取目录中的所有文件夹，并按字母顺序排序
    folders = sorted(os.listdir(directory_path))
    result_list = []

    for i, folder in enumerate(folders):
        if os.path.isdir(os.path.join(directory_path, folder)):  # 确保是文件夹
            category_number = assign_category_number(folder)
            if category_number != -1:
                result_list.append(f"{folder}\t{i}\t{category_number}")

    # 将结果写入txt文件
    with open("label.txt", "w") as f:
        for item in result_list:
            f.write(item + "\n")

    return result_list


# 设定目标目录路径
directory_path = "garbage"

# 执行操作并生成结果文件
results = main(directory_path)
print("操作完成，结果已保存到label.txt文件中。")
