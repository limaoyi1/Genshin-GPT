# 爬取 https://genshindb-ia.netlify.app/ 数据
# 通过查询可以确保更新数据
import os

import requests
import json


def save_json_from_api(api_template_url, replace_content, save_path):
    try:
        # 构建完整的API URL
        api_url = api_template_url.replace("abcdefg", replace_content)

        # 发送GET请求获取JSON数据
        response = requests.get(api_url)
        response.raise_for_status()  # 检查请求是否成功
        data = response.json()

        # 确保保存数据的目录存在
        os.makedirs(os.path.dirname(save_path), exist_ok=True)

        # 将JSON数据保存到本地文件
        with open(save_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=2)

        print("JSON数据已成功保存到:", save_path)

    except requests.exceptions.RequestException as e:
        print("请求出错:", e)
    except json.JSONDecodeError as e:
        print("JSON解析出错:", e)
    except Exception as e:
        print("发生了一个未知错误:", e)


if __name__ == "__main__":
    # 替换这里的内容为实际需要的内容
    replace_contents = ["characters", "talents", "constellations", "outfits", "weapons", "foods", "materials",
                        "artifacts", "domains", "enemies", "rarity", "elements", "achievements", "achievementgroups", "windgliders",
                        "animals", "namecards", "geographies", "adventureranks"]
    api_template_url = "https://genshin-db-api.vercel.app/api/" \
                       "abcdefg?query=names&matchAliases=true&matchCategories=true&verboseCategories=true" \
                       "&queryLanguages=ChineseSimplified,English&resultLanguage=ChineseSimplified"
    save_path = "../resource/genshindb/weapons.json"
    for item in replace_contents:
        save_path = "../resource/genshindb/"+ item+".json"
        save_json_from_api(api_template_url, item, save_path)

# "rarity", "elements" 无所谓 ,反正"enemies"中有