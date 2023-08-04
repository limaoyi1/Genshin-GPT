# pdf 的 格式太难以处理了 乱版和乱码过于损害数据


# import os
# import re
#
# import requests
#
#
# def download_pdf(url, save_folder):
#     response = requests.get(url)
#     if response.status_code == 200:
#         # 提取文件名
#         file_name = url.split("/")[-1]
#         if not file_name.endswith(".pdf"):
#             file_name += ".pdf"
#         save_path = os.path.join(save_folder, file_name)
#
#         # 保存文件
#         with open(save_path, "wb") as f:
#             f.write(response.content)
#     else:
#         print(f"下载失败：{url}")
#         download_pdf2(url.replace("_(原神)", ""), save_folder)
#
#
# def download_pdf2(url, save_folder):
#     response = requests.get(url)
#     if response.status_code == 200:
#         # 提取文件名
#         file_name = url.split("/")[-1]
#         if not file_name.endswith(".pdf"):
#             file_name += ".pdf"
#         save_path = os.path.join(save_folder, file_name)
#
#         # 保存文件
#         with open(save_path, "wb") as f:
#             f.write(response.content)
#     else:
#         print(f"下载失败：{url}")
#
#
# def batch_download_pdf(urls, save_folder):
#     # 创建保存文件夹
#     if not os.path.exists(save_folder):
#         os.makedirs(save_folder)
#
#     # 逐个下载PDF
#     for url in urls:
#         download_pdf(url, save_folder)
#
#
# def extract_names_from_code(code):
#     name_regex = r'\bname:\s*"([^"]+)"'
#     names = re.findall(name_regex, code)
#     return names
#
# if __name__ == "__main__":
#     # 要下载的PDF链接列表
#     names = ['纳西妲', '绮良良', '卡维', '白术', '卡米', '迪希雅', '瑶瑶', '散兵', '艾尔海森', '空', '荧', '温迪', '安柏', '凯亚', '迪卢克', '丽莎', '琴', '莫娜', '芭芭拉', '班尼特', '迪奥娜', '诺艾尔', '菲谢尔', '砂糖', '罗莎莉亚', '优菈', '雷泽', '可莉', '阿贝多', '钟离', '魈', '甘雨', '胡桃', '七七', '刻晴', '刻晴2', '香菱', '行秋', '重云', '凝光', '凝光', '北斗', '申鹤', '云堇', '辛焱', '夜兰', '埃洛伊', '达达利亚', '雷电将军', '枫原万叶', '神里绫华', '宵宫', '神里绫人', '珊瑚宫心海', '五郎', '八重神子', '九条裟罗', '托马', '荒泷一斗', '久岐忍', '早柚', '鹿野院平藏', '提纳里', '柯莱', '赛诺', '坎蒂丝', '多莉', '妮露', '莱依拉', '珐露珊']
#
#     urls = []
#     for name in names:
#         url = "https://zh.wikipedia.org/api/rest_v1/page/pdf/" + name + "_(原神)"
#         urls.append(url)
#
#     # 保存PDF的文件夹路径
#     save_folder = "./../resource/pdf_files"
#
#     # 批量下载PDF
#     batch_download_pdf(urls, save_folder)
