#os是python的文件系统模块
import os
# print(os.listdir("D:/"))  # 列出路径下的内容
# print(os.path.isdir("D:/BaiduNetdisk")) # 判断指定路径是不是文件夹
# print(os.path.exists("D:/BaiduNetdisk"))    # 判断路径是否存在
def get_files(path):
    file_list = []
    if os.path.exists(path):
        try:
            for f in os.listdir(path):
                full_path = os.path.join(path, f)#将path和f合成完整路径
                if os.path.isdir(full_path):
                    try:
                        sub_files = get_files(full_path)
                        file_list.extend(sub_files)
                    except PermissionError:
                        print(f"无法访问文件夹: {full_path}")
                else:
                    file_list.append(full_path)
        except PermissionError:
            print(f"在列出目录内容时遇到权限问题: {path}")
            # return file_list  # 如果要返回已找到的文件，取消注释这行代码
    else:
        print(f"指定的目录{path}不存在")
        return []
    return file_list

if __name__ == '__main__':
    with open("files.txt", "w", encoding="utf-8") as f:
        file_data = get_files("d:/")
        for file_path in file_data:
            f.write(file_path + "\n")
