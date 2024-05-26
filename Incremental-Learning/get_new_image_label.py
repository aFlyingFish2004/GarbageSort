import os

# 该代码用于生成新增数据集的标签文件label.txt，文件内容格式如下：

# 假设您的标签文档是一个纯文本文件
label_file = "label.txt"
# 创建一个字典，将类别映射到标签
label_dict = {}
with open(label_file, "r", encoding="utf-8") as f:
    for line in f:
        parts = line.strip().split("\t")
        pre = parts[0].strip().split("_")
        category = pre[1]  # 类别
        label = int(parts[1])  # 标签
        label_dict[category] = label

# 指定上传文件夹路径
output_file = "./Incremental-Learning/incremental.txt"
error_log = "error_log.txt"

# 定义有效的图片扩展名
valid_image_extensions = {".jpg", ".jpeg", ".png", ".bmp", ".gif"}


def rename_files_in_directory(directory):
    parent_folder = os.path.basename(directory)
    parts = parent_folder.split("_")
    files = sorted(os.listdir(directory))
    for idx, file in enumerate(files, start=1):
        file_path = os.path.join(directory, file)
        if os.path.isfile(file_path):
            file_extension = os.path.splitext(file)[1].lower()
            if file_extension in valid_image_extensions:
                new_file_name = f"img_{parts[1]}_{idx}{file_extension}"
                new_file_path = os.path.join(directory, new_file_name)
                print(new_file_path)
                os.rename(file_path, new_file_path)
            else:
                os.remove(file_path)
                print(f"Deleted non-image file: {file_path}")


with open(output_file, "w", encoding="utf-8") as f_out, open(
    error_log, "w", encoding="utf-8"
) as f_err:
    for root, dirs, files in os.walk("upload/feedback"):
        dirs.sort()
        files.sort()
        try:
            for file in files:
                file_path = os.path.join(root, file)
                file_extension = os.path.splitext(file)[1].lower()
                if file_extension not in valid_image_extensions:
                    os.remove(file_path)
                    print(f"Deleted non-image file: {file_path}")
                    continue

                parts = file.split("_")
                if len(parts) < 2:
                    raise IndexError(f"文件名格式错误: {file}")
                category = parts[1]
                label = label_dict.get(category, None)
                if label is not None:
                    f_out.write(f"{file_path}\t{label}\n")
        except IndexError as e:
            print(f"IndexError: 检测到错误的目录: {root}, 错误信息: {str(e)}")
            f_err.write(f"IndexError: 检测到错误的目录: {root}, 错误信息: {str(e)}\n")
            rename_files_in_directory(root)
            break
        except Exception as e:
            print(f"Exception: 检测到错误的目录: {root}, 错误信息: {str(e)}")
            f_err.write(f"Exception: 检测到错误的目录: {root}, 错误信息: {str(e)}\n")
            break

print(f"文件路径和标签已写入 {output_file}")
print(f"错误日志已写入 {error_log}")
