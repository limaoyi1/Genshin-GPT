import os
from urllib.parse import quote

from train.match import MatchAnswer


if __name__ == "__main__":
    answer = MatchAnswer("优菈")
    matchs = answer.matchWiki("故事")
    print(matchs)

# if __name__ == "__main__":
#     namesv1 = ['纳西妲', '绮良良', '卡维', '白术', '卡米', '迪希雅', '瑶瑶', '散兵', '艾尔海森', '空', '荧', '温迪', '安柏',
#              '凯亚', '迪卢克', '丽莎', '琴', '莫娜', '芭芭拉', '班尼特', '迪奥娜', '诺艾尔', '菲谢尔', '砂糖', '罗莎莉亚',
#              '优菈', '雷泽', '可莉', '阿贝多', '钟离', '魈', '甘雨', '胡桃', '七七', '刻晴', '刻晴2', '香菱', '行秋',
#              '重云', '凝光', '凝光', '北斗', '申鹤', '云堇', '辛焱', '夜兰', '埃洛伊', '达达利亚', '雷电将军', '枫原万叶',
#              '神里绫华', '宵宫', '神里绫人', '珊瑚宫心海', '五郎', '八重神子', '九条裟罗', '托马', '荒泷一斗', '久岐忍',
#              '早柚', '鹿野院平藏', '提纳里', '柯莱', '赛诺', '坎蒂丝', '多莉', '妮露', '莱依拉', '珐露珊']
#     names =["提瓦特编年史","北陆图书馆","过场提示","黑话"]
#     links = []
#     for name in names:
#         link = "https://wiki.biligame.com/ys/"+quote(name, safe='')
#         links.append(link)
#     print(links)



# def change_txt_to_md_in_folder(folder_path):
#     for root, dirs, files in os.walk(folder_path):
#         for file in files:
#             if file.endswith(".txt"):
#                 old_file_path = os.path.join(root, file)
#                 new_file_path = os.path.join(root, file[:-4] + ".md")
#                 os.rename(old_file_path, new_file_path)
#                 print(f"文件已成功重命名：{old_file_path} -> {new_file_path}")

# # 测试
# if __name__ == "__main__":
#     folder_path_to_change = "./resource/wiki"  # 替换为实际的文件夹路径
#     change_txt_to_md_in_folder(folder_path_to_change)

# def get_py_files_in_path(path):
#     py_files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f)) and f.endswith('.pdf')]
#     return py_files
#
#
# if __name__ == "__main__":
#     # 获取路径中的所有文件
#     # 示例用法
#     path = './resource/pdf_files'  # 替换为你想要查找的目录的路径
#     py_files_list = get_py_files_in_path(path)
#     link =[]
#     for file in py_files_list:
#         file = "https://zh.wikipedia.org/wiki/"+file.replace(".pdf", "")
#         file = quote(file, safe='').replace("%3A",":").replace("%2F","/")
#         link.append(file)
#         print(file)
#     print(link)
#     print(len(link))

# if __name__ == "__main__":
#     answer = MatchAnswer("钟离")
#     matchs = answer.match("早安")
#     print(matchs)


# def number_to_letter(number):
#     if not 1 <= number <= 100:
#         raise ValueError("Number must be between 1 and 100")
#
#     if number <= 26:
#         # Convert the number to a letter using the same method as before
#         letter = chr(number + 64)
#     else:
#         # For numbers between 27 and 100, convert the tens and ones digits separately
#         tens_digit = (number - 1) // 26
#         ones_digit = (number - 1) % 26
#         tens_letter = chr(tens_digit + 65) if tens_digit > 0 else ""
#         ones_letter = chr(ones_digit + 65)
#         letter = f"{tens_letter}{ones_letter}"
#
#     return letter
#
#
# ii = 74
# for i in range(ii):
#     if i < 9:
#         print(f"""import {number_to_letter(i + 1)}Avatar from \"../assets/1000{i + 1}.webp\";""")
#     else:
#         print(f"""import {number_to_letter(i + 1)}Avatar from \"../assets/100{i + 1}.webp\";""")
#
# for i in range(ii):
#     print(f"""export const {number_to_letter(i + 1)}Model = {{
#     name: "{number_to_letter(i + 1)}",
#     avatar: {number_to_letter(i + 1)}Avatar
# }};
#     """)
#
# print("export const users = [")
#
# for i in range(ii):
#     print(f"""{number_to_letter(i + 1)}Model,""")
# print("];")
