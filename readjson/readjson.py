################################################
#                                              #
#                                              #
#               对原始数据进行处理                 #
#                                              #
#                                              #
################################################
import json

from readjson.jsonclass import Dialog, Handed

# 加载JSON文件并解析为Python对象
with open(file='./../resource/result.json', mode='r', encoding="utf-8") as file:
    json_data = json.load(file)

# 使用解析得到的Python对象实例化类
dialogs = []
for dialog_id, dialog_data in json_data.items():
    dialog = Dialog(
        dialog_id,
        dialog_data.get('fileName', ''),
        dialog_data.get('language', ''),
        dialog_data.get('npcName', ''),  # 使用get方法来获取npcName属性，如果不存在则返回空字符串
        dialog_data.get('text', ''),
        dialog_data.get('type', '')
    )
    dialogs.append(dialog)

i = 0
# 打印每个对话对象的属性
for dialog in dialogs:
    # print(f"ID: {dialog.id}")
    # print(f"File Name: {dialog.fileName}")
    # print(f"Language: {dialog.language}")
    # print(f"NPC Name: {dialog.npcName}")
    # print(f"Text: {dialog.text}")
    # print(f"Type: {dialog.type}")
    # print()
    i = i + 1
print(i)  # 367884 条


out: list[Handed] = []
out_chs: list[Handed] = []
out_en: list[Handed] = []
# 过滤掉日语,韩语,id,文件路径

i = 0
for dialog in dialogs:
    if dialog.language == 'KR' or dialog.language == 'JP':
        continue
    headed = Handed(dialog.language, dialog.npcName, dialog.text, dialog.type)
    out.append(headed)
    if dialog.language == 'CHS':
        out_chs.append(headed)
    elif dialog.language == 'EN':
        out_en.append(headed)
    i = i + 1
print(i)

# 将列表 l 保存为 JSON 文件
with open('./../resource/output.json', 'w', encoding='utf-8') as file:
    json.dump([obj.__dict__ for obj in out], file, ensure_ascii=False, indent=2)

with open('./../resource/output_chs.json', 'w', encoding='utf-8') as file:
    json.dump([obj.__dict__ for obj in out_chs], file, ensure_ascii=False, indent=2)

with open('./../resource/output_en.json', 'w', encoding='utf-8') as file:
    json.dump([obj.__dict__ for obj in out_en], file, ensure_ascii=False, indent=2)
# 101M ===> 32M
