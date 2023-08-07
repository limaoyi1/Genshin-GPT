import os


def delete_data_between_strings(input_string, start_string, end_string):
    # 找到开始字符串的索引
    start_index = input_string.find(start_string)
    while start_index != -1:
        # 找到结束字符串的索引
        end_index = input_string.find(end_string, start_index)
        if end_index != -1:
            # 删除开始字符串到结束字符串之间的数据，包括开始和结束字符串
            input_string = input_string[:start_index] + input_string[end_index + len(end_string):]
            # 继续寻找下一个开始字符串的索引
            start_index = input_string.find(start_string, start_index)
        else:
            # 如果找不到结束字符串，则结束循环
            break

    return input_string

# 定义删除数据的函数，代码同上

def process_md_files_in_directory(directory_path, start_string, end_string):
    # 获取目录下所有文件和子目录的列表
    all_files = os.listdir(directory_path)

    for file_name in all_files:
        # 拼接完整文件路径
        file_path = os.path.join(directory_path, file_name)

        # 检查是否为md文件
        if file_name.endswith(".md") and os.path.isfile(file_path):
            # 读取文件内容
            with open(file_path, 'r') as file:
                content = file.read()

            # 执行删除操作
            processed_content = delete_data_between_strings(content, start_string, end_string)

            # 将处理后的内容写回文件
            with open(file_path, 'w') as file:
                file.write(processed_content)


# 指定目录和删除字符串
directory_path = "/path/to/your/directory"
start_string = "aaa"
end_string = "bbb"

# 执行处理
process_md_files_in_directory(directory_path, start_string, end_string)