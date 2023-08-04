class Character:
    def __init__(self, name="", fullname="", title="", description="", rarity="",
                 element="", weapontype="", substat="", gender="", body="",
                 association="", region="", affiliation="", birthdaymmdd="",
                 birthday="", constellation="", cv=None, costs=None, images=None,
                 url=None, stats=None, version=""):
        self.name = name
        self.fullname = fullname
        self.title = title
        self.description = description
        self.rarity = rarity
        self.element = element
        self.weapontype = weapontype
        self.substat = substat
        self.gender = gender
        self.body = body
        self.association = association
        self.region = region
        self.affiliation = affiliation
        self.birthdaymmdd = birthdaymmdd
        self.birthday = birthday
        self.constellation = constellation
        self.cv = cv if cv is not None else {
            "english": "",
            "chinese": "",
            "japanese": "",
            "korean": ""
        }
        self.costs = costs if costs is not None else {
            "ascend1": [],
            "ascend2": [],
            "ascend3": [],
            "ascend4": [],
            "ascend5": [],
            "ascend6": []
        }
        self.images = images if images is not None else {
            "nameicon": "",
            "namesideicon": "",
            "namegachasplash": "",
            "namegachaslice": "",
            "card": "",
            "portrait": "",
            "icon": "",
            "sideicon": "",
            "cover1": "",
            "cover2": "",
            "hoyolab-avatar": ""
        }
        self.url = url if url is not None else {
            "fandom": ""
        }
        self.stats = stats
        self.version = version

    def get_chinese_message(self):
        message = f"名字是{self.name}, " \
                  f"全名是{self.fullname}, " \
                  f"头衔是{self.title}, " \
                  f"简介为{self.description}, " \
                  f"稀有度为{self.rarity}, " \
                  f"属性为{self.element}, " \
                  f"武器类型为{self.weapontype}, " \
                  f"副属性为{self.substat}, " \
                  f"性别为{self.gender}, " \
                  f"体型为{self.body}, " \
                  f"关联为{self.association}, " \
                  f"所在地区为{self.region}, " \
                  f"所属机构为{self.affiliation}, " \
                  f"生日为{self.birthdaymmdd}, " \
                  f"出生日期为{self.birthday}, " \
                  f"命座为{self.constellation}, " \
                  f"CV为{self.cv['chinese']}. " \
            # f"图片URL为{self.images['nameicon']}, " \
        # f"相关链接为{self.url['fandom']}"

        return message


class Achievementgroups:
    def __init__(self, name="", sortorder=0, reward=None, images=None, version=""):
        self.name = name
        self.sortorder = sortorder
        self.reward = reward if reward is not None else {"name": ""}
        self.images = images if images is not None else {"nameicon": ""}
        self.version = version

    def get_message_chinese(self):
        message = f"成就组名：{self.name}\n" \
                  f"排序编号：{self.sortorder}\n" \
                  f"奖励名片：{self.reward.get('name', '')}\n" \
                  f"版本号：{self.version}"
        # f"图片名称图标：{self.images.get('nameicon', '')}\n" \


class Achievements:
    def __init__(self, name="", achievementgroup="", ishidden=False, sortorder=0, stages=0,
                 stage1=None, version=""):
        self.name = name
        self.achievementgroup = achievementgroup
        self.ishidden = ishidden
        self.sortorder = sortorder
        self.stages = stages
        self.stage1 = stage1 if stage1 is not None else {}
        self.version = version

    def get_message_chinese(self):
        message = f"成就名：{self.name}\n" \
                  f"成就组：{self.achievementgroup}\n" \
                  f"是否隐藏：{self.ishidden}\n" \
                  f"排序编号：{self.sortorder}\n" \
                  f"阶段数量：{self.stages}\n" \
                  f"阶段1标题：{self.stage1.get('title', '')}\n" \
                  f"阶段1描述：{self.stage1.get('description', '')}\n" \
                  f"阶段1进度：{self.stage1.get('progress', 0)}\n" \
                  f"阶段1奖励：{self.stage1.get('reward', {})}\n" \
                  f"版本号：{self.version}"
        return message


class AdventurerRank:
    def __init__(self, name="", exp=0, unlockdescription="", reward=None, version=""):
        self.name = name
        self.exp = exp
        self.unlockdescription = unlockdescription
        self.reward = reward if reward is not None else []
        self.version = version

    def get_message_chinese(self):
        rewards_str = ', '.join(self.get_reward_strings()) if self.reward else "无"
        message = f"冒险等级：{self.name}\n" \
                  f"所需经验：{self.exp}\n" \
                  f"解锁描述：{self.unlockdescription}\n" \
                  f"奖励：{rewards_str}\n" \
                  f"版本号：{self.version}"
        return message

    def get_reward_strings(self):
        reward_strings = []
        for reward_item in self.reward:
            reward_name = reward_item.get('name', '')
            reward_count = reward_item.get('count', 0)
            reward_string = f"{reward_name} x{reward_count}"
            reward_strings.append(reward_string)
        return reward_strings


class Animal:
    def __init__(self, name="", description="", category="", counttype="", sortorder=0, images=None, version=""):
        self.name = name
        self.description = description
        self.category = category
        self.counttype = counttype
        self.sortorder = sortorder
        self.images = images if images is not None else {}
        self.version = version

    def get_message_chinese(self):
        message = f"动物名：{self.name}\n" \
                  f"描述：{self.description}\n" \
                  f"类别：{self.category}\n" \
                  f"计数类型：{self.counttype}\n" \
                  f"排序编号：{self.sortorder}\n" \
                  f"图片URL：{self.images.get('nameicon', '')}\n" \
                  f"版本号：{self.version}"
        return message


class Artifact:
    def __init__(self, name="", rarity=[], set_bonus=None, flower=None):
        self.name = name
        self.rarity = rarity
        self.set_bonus = set_bonus if set_bonus is not None else {}
        self.flower = flower if flower is not None else {}

    def get_message_chinese(self):
        rarity_str = ', '.join(self.rarity)
        set_bonus_str = f"2件套效果：{self.set_bonus.get('2pc', '')}\n4件套效果：{self.set_bonus.get('4pc', '')}"

        message = f"圣遗物名：{self.name}\n" \
                  f"稀有度：{rarity_str}\n" \
                  f"套装效果：\n{set_bonus_str}\n"

        if self.flower:
            message += f"花之圣遗物：\n" \
                       f"名称：{self.flower.get('name', '')}\n" \
                       f"遗物类型：{self.flower.get('relictype', '')}\n" \
                       f"描述：{self.flower.get('description', '')}\n" \
                       f"背景故事：{self.flower.get('story', '')}\n"

        return message


class Constellation:
    def __init__(self, name="", effect="", images=None, c1=None, c2=None, c3=None, c4=None, c5=None, c6=None):
        self.name = name
        self.effect = effect
        self.images = images if images is not None else {}
        self.c1 = c1 if c1 is not None else {}
        self.c2 = c2 if c2 is not None else {}
        self.c3 = c3 if c3 is not None else {}
        self.c4 = c4 if c4 is not None else {}
        self.c5 = c5 if c5 is not None else {}
        self.c6 = c6 if c6 is not None else {}

    def get_message_chinese(self):
        message = f"命座名称：{self.name}\n" \
                  f"效果：{self.effect}\n" \
                  f"图片URL：{self.images.get(self.name.lower(), '')}\n" \
                  f"c1效果：{self.c1.get('effect', '无')}\n" \
                  f"c2效果：{self.c2.get('effect', '无')}\n" \
                  f"c3效果：{self.c3.get('effect', '无')}\n" \
                  f"c4效果：{self.c4.get('effect', '无')}\n" \
                  f"c5效果：{self.c5.get('effect', '无')}\n" \
                  f"c6效果：{self.c6.get('effect', '无')}\n"
        return message


class Domain:
    def __init__(self, name="", region="", domain_entrance="", domain_type="", description="",
                 recommended_level=0, recommended_elements=None, unlock_rank=0, reward_preview=None,
                 disorder=None, monster_list=None, images=None, version=""):
        self.name = name
        self.region = region
        self.domain_entrance = domain_entrance
        self.domain_type = domain_type
        self.description = description
        self.recommended_level = recommended_level
        self.recommended_elements = recommended_elements if recommended_elements is not None else []
        self.unlock_rank = unlock_rank
        self.reward_preview = reward_preview if reward_preview is not None else []
        self.disorder = disorder if disorder is not None else []
        self.monster_list = monster_list if monster_list is not None else []
        self.images = images if images is not None else {}
        self.version = version

    def get_message_chinese(self):
        # 获取奖励预览信息
        reward_preview_str = ""
        for reward in self.reward_preview:
            if 'count' in reward:
                reward_preview_str += f"{reward['name']} x {reward['count']}\n"
            else:
                reward_preview_str += f"{reward['name']}\n"

        # 获取其他信息
        disorder_str = "\n".join(self.disorder) if self.disorder else "无"

        # 构建消息
        message = f"副本名称：{self.name}\n" \
                  f"所在地区：{self.region}\n" \
                  f"入口位置：{self.domain_entrance}\n" \
                  f"副本类型：{self.domain_type}\n" \
                  f"描述：{self.description}\n" \
                  f"推荐等级：{self.recommended_level}\n" \
                  f"推荐元素：{', '.join(self.recommended_elements)}\n" \
                  f"解锁等级：{self.unlock_rank}\n" \
                  f"奖励预览：\n{reward_preview_str}" \
                  f"扰动效果：\n{disorder_str}\n" \
                  f"怪物列表：{', '.join(self.monster_list)}\n" \
                  f"副本图片：{self.images['namepic']}"

        return message


class Enemies:
    def __init__(self, data):
        self.name = data.get('name', "")
        self.specialname = data.get('specialname', "")
        self.enemytype = data.get('enemytype', "")
        self.category = data.get('category', "")
        self.description = data.get('description', "")
        self.rewardpreview = data.get('rewardpreview', [])
        self.images = data.get('images', {})
        self.version = data.get('version', "")

    def get_message_chinese(self):
        message = f"名称：{self.name}\n"
        message += f"特殊名称：{self.specialname}\n"
        message += f"敌人类型：{self.enemytype}\n"
        message += f"类别：{self.category}\n"
        message += f"描述：{self.description}\n"
        print(self.rewardpreview)
        if self.rewardpreview:
            message += "奖励预览：\n"
            for reward in self.rewardpreview:
                reward_name = reward.get('name', "")
                reward_rarity = reward.get('rarity', "")
                reward_count = reward.get('count', None)
                if reward_count is None:
                    message += f"{reward_name}（稀有度：{reward_rarity}）\n"
                else:
                    message += f"{reward_name} x {reward_count}（稀有度：{reward_rarity}）\n"
        else:
            message += "奖励预览：无\n"

        return message

import json

class Food:
    def __init__(self, data):
        self.name = data['name']
        self.rarity = data['rarity']
        self.foodtype = data['foodtype']
        self.foodfilter = data['foodfilter']
        self.foodcategory = data['foodcategory']
        self.effect = data['effect']
        self.description = data['description']
        self.suspicious = data.get('suspicious', {})
        self.normal = data.get('normal', {})
        self.delicious = data.get('delicious', {})
        self.ingredients = data['ingredients']
        self.images = data['images']
        self.version = data['version']

    def get_message_chinese(self):
        ingredients_str = ", ".join(
            ["{} x {}".format(ingredient["name"], ingredient["count"]) for ingredient in self.ingredients])
        result = "所需材料：" + ingredients_str + "\n"
        return (
            f"名称：{self.name}\n"
            f"稀有度：{self.rarity}\n"
            f"食物类型：{self.foodtype}\n"
            f"食物过滤器：{self.foodfilter}\n"
            f"食物分类：{self.foodcategory}\n"
            f"效果：{self.effect}\n"
            f"描述：{self.description}\n"
            f"可疑品效果：{self.suspicious.get('effect', '无')}\n"
            f"可疑品描述：{self.suspicious.get('description', '无')}\n"
            f"普通品效果：{self.normal.get('effect', '无')}\n"
            f"普通品描述：{self.normal.get('description', '无')}\n"
            f"美味品效果：{self.delicious.get('effect', '无')}\n"
            f"美味品描述：{self.delicious.get('description', '无')}\n"
            f"所需材料：" + ingredients_str + "\n"
            f"图片链接：{self.images.get('nameicon', '无')}\n"
            f"版本：{self.version}\n"
        )

    def __str__(self):
        return self.get_message_chinese()


class Geography:
    def __init__(self, data):
        self.name = data.get('name', '')
        self.area = data.get('area', '')
        self.description = data.get('description', '')
        self.region = data.get('region', '')
        self.showonlyunlocked = data.get('showonlyunlocked', False)
        self.sortorder = data.get('sortorder', 0)

    def get_message_chinese(self):
        return f"特殊名称：{self.name}\n地区：{self.area}\n描述：{self.description}"


class Material:
    def __init__(self, data):
        self.name = data.get('name', '')
        self.description = data.get('description', '')
        self.sortorder = data.get('sortorder', 0)
        self.rarity = data.get('rarity', '')
        self.category = data.get('category', '')
        self.materialtype = data.get('materialtype', '')
        self.source = data.get('source', [])
        self.images = data.get('images', {})
        self.url = data.get('url', {})

    def get_message_chinese(self):
        return f"名称：{self.name}\n" \
               f"描述：{self.description}\n" \
               f"稀有度：{self.rarity}\n" \
               f"类型：{self.materialtype}\n" \
               f"来源：{', '.join(self.source)}\n" \
               f"图片链接：{self.images.get('fandom', '')}\n" \
               f"详情链接：{self.url.get('fandom', '')}"

class NameCard:
    def __init__(self, data):
        self.name = data.get('name', '')
        self.description = data.get('description', '')
        self.sortorder = data.get('sortorder', 0)
        self.source = data.get('source', [])
        self.images = data.get('images', {})
        self.version = data.get('version', '')

    def get_message_chinese(self):
        return f"名片名称：{self.name}\n描述：{self.description}\n来源：{', '.join(self.source)}"

class Outfit:
    def __init__(self, data):
        self.name = data.get('name', '')
        self.description = data.get('description', '')
        self.is_default = data.get('isdefault', False)
        self.character = data.get('character', '')
        self.source = data.get('source', [])
        self.images = data.get('images', {})
        self.url = data.get('url', {})
        self.version = data.get('version', '')

    def get_message_chinese(self):
        return f"装扮名称：{self.name}\n" \
               f"描述：{self.description}\n" \
               f"是否默认：{'是' if self.is_default else '否'}\n" \
               f"角色：{self.character}\n" \
               f"来源：{', '.join(self.source)}\n" \
               f"版本：{self.version}"

class Talent:
    def __init__(self, talent_data):
        self.name = talent_data["name"]
        self.combat1 = Combat(talent_data.get("combat1", {}))
        self.combat2 = Combat(talent_data.get("combat2", {}))
        self.combat3 = Combat(talent_data.get("combat3", {}))
        self.passive1 = Passive(talent_data.get("passive1", {}))
        self.passive2 = Passive(talent_data.get("passive2", {}))
        self.passive3 = Passive(talent_data.get("passive3", {}))

    def run(self, name):
        if self.name == name:
            return self.get_message_chinese()
        return f"未找到名为'{name}'的天赋信息。"

    def get_message_chinese(self):
        message = f"**{self.name}**\n\n"
        message += f"**{self.combat1.name}**\n{self.combat1.info}\n\n{self.combat1.get_attributes_chinese()}\n\n"
        message += f"**{self.combat2.name}**\n{self.combat2.info}\n\n{self.combat2.get_attributes_chinese()}\n\n"
        message += f"**{self.combat3.name}**\n{self.combat3.info}\n\n{self.combat3.get_attributes_chinese()}\n\n"
        message += f"**{self.passive1.name}**\n{self.passive1.info}\n\n"
        message += f"**{self.passive2.name}**\n{self.passive2.info}\n\n"
        message += f"**{self.passive3.name}**\n{self.passive3.info}"
        return message


class Combat:
    def __init__(self, combat_data):
        self.name = combat_data.get("name", "")
        self.info = combat_data.get("info", "")
        self.attributes = combat_data.get("attributes", {})

    def get_attributes_chinese(self):
        attributes_str = ""
        param_keys = [f"param{i+1}" for i in range(len(self.attributes["labels"]))]
        parameters = dict(zip(param_keys, self.attributes["parameters"]))

        for label in self.attributes["labels"]:
            # todo 具体数据以后再处理
            attributes_str += f"{label}\n"  # Updated format specifier
        return attributes_str


class Passive:
    def __init__(self, passive_data):
        self.name = passive_data.get("name", "")
        self.info = passive_data.get("info", "")

class Weapon:
    def __init__(self, name="", description="", weapontype="", rarity="",
                 story="", baseatk=0, substat="", subvalue=0, effectname="",
                 effect="", r1=None, r2=None, r3=None, r4=None, r5=None,
                 weaponmaterialtype="", costs=None, images=None, url=None,
                 version=""):
        self.name = name
        self.description = description
        self.weapontype = weapontype
        self.rarity = rarity
        self.story = story
        self.baseatk = baseatk
        self.substat = substat
        self.subvalue = subvalue
        self.effectname = effectname
        self.effect = effect
        self.r1 = r1 if r1 is not None else []
        self.r2 = r2 if r2 is not None else []
        self.r3 = r3 if r3 is not None else []
        self.r4 = r4 if r4 is not None else []
        self.r5 = r5 if r5 is not None else []
        self.weaponmaterialtype = weaponmaterialtype
        self.costs = costs if costs is not None else {}
        self.images = images if images is not None else {}
        self.url = url if url is not None else {}
        self.version = version

    def get_message_chinese(self):
        message = f"武器名称: {self.name}\n"
        message += f"武器类型: {self.weapontype}\n"
        message += f"稀有度: {self.rarity}星\n"
        message += f"基础攻击力: {self.baseatk}\n"
        message += f"副属性: {self.substat} +{self.subvalue}\n"
        message += f"特效名称: {self.effectname}\n"
        message += f"特效: {self.effect}\n"

        if self.r1:
            message += f"\n精炼等级属性加成:\n"
            message += f"R1: {self.r1[0]}  伤害加成: {self.r1[1]}\n"
            message += f"R2: {self.r2[0]}  伤害加成: {self.r2[1]}\n"
            message += f"R3: {self.r3[0]}  伤害加成: {self.r3[1]}\n"
            message += f"R4: {self.r4[0]}  伤害加成: {self.r4[1]}\n"
            message += f"R5: {self.r5[0]}  伤害加成: {self.r5[1]}\n"

        if self.costs:
            message += f"\n升星材料消耗:\n"
            for ascend, materials in self.costs.items():
                message += f"{ascend.capitalize()}升星:\n"
                for material in materials:
                    message += f"{material['name']}: {material['count']}\n"

        return message

class Windglider:
    def __init__(self, name="", description="", rarity="", story="", sortorder=0,
                 source=None, images=None, version=""):
        self.name = name
        self.description = description
        self.rarity = rarity
        self.story = story
        self.sortorder = sortorder
        self.source = source if source is not None else []
        self.images = images if images is not None else {}
        self.version = version

    def get_message_chinese(self):
        message = f"风之翼名称: {self.name}\n"
        message += f"稀有度: {self.rarity}星\n"
        message += f"描述: {self.description}\n"
        message += f"获取途径: {', '.join(self.source)}\n"
        return message