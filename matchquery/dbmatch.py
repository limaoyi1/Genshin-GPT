import json

from download.dbclass import Character, Achievementgroups, Achievements, AdventurerRank, Animal, Artifact, \
    Constellation, Domain, Enemies, Food, Geography, Material, NameCard, Outfit, Talent, Weapon, Windglider


class CharacterWrapper:
    characters: list[Character] = []

    def __init__(self, path="./resource/genshindb/characters.json"):
        # 将json实例化为list
        with open(path, 'r', encoding='utf-8') as file:
            character_data = json.load(file)

        for data in character_data:
            character = Character()
            character.name = data['name']
            character.fullname = data['fullname']
            character.title = data['title']
            character.description = data['description']
            character.rarity = data['rarity']
            character.element = data['element']
            character.weapontype = data['weapontype']
            character.substat = data['substat']
            character.gender = data['gender']
            character.body = data['body']
            character.association = data['association']
            character.region = data['region']
            character.affiliation = data['affiliation']
            character.birthdaymmdd = data['birthdaymmdd']
            character.birthday = data['birthday']
            character.constellation = data['constellation']
            character.cv = data['cv']
            character.costs = data['costs']
            character.images = data['images']
            # character.url = data['url']
            # character.stats = data['stats']
            character.version = data['version']

            self.characters.append(character)

    def run(self, name):
        # 通过名字查询角色信息
        for character in self.characters:
            if character.name == name:
                return character.get_chinese_message()
        return f"未找到名为'{name}'的角色信息。"

    def query_character_info(self, name):
        for character in self.characters:
            if character.name == name:
                return character.description
        print(f"未找到名为'{character}'的角色信息。")


class AchievementgroupsWrapper:
    groups: list[Achievementgroups] = []

    def __init__(self, path="./resource/genshindb/achievementgroups.json"):
        with open(path, 'r', encoding='utf-8') as file:
            groups_data = json.load(file)

        for data in groups_data:
            group = Achievementgroups(
                name=data['name'],
                sortorder=data['sortorder'],
                reward=data.get('reward', ""),
                images=data['images'],
                version=data['version']
            )
            self.groups.append(group)

    def get_achievement_groups_info(self, name):
        # 通过名字查询成就信息
        for group in self.groups:
            if group.name == name:
                return group.get_message_chinese()
        return f"未找到名为'{name}'的成就分组信息。"

    def run(self, name):
        return self.get_achievement_groups_info(name)


class AchievementsWrapper:
    achievements: list[Achievements] = []

    def __init__(self, path="./resource/genshindb/achievements.json"):
        with open(path, 'r', encoding='utf-8') as file:
            achievements_data = json.load(file)

        for data in achievements_data:
            achievement = Achievements(
                name=data['name'],
                achievementgroup=data['achievementgroup'],
                ishidden=data.get('ishidden', False),
                sortorder=data['sortorder'],
                stages=data['stages'],
                stage1=data['stage1'],
                version=data['version']
            )

            self.achievements.append(achievement)

    def get_achievement_info(self, name):
        # 通过名字查询成就信息
        for achievement in self.achievements:
            if achievement.name == name:
                return achievement.get_message_chinese()
        return f"未找到名为'{name}'的成就信息。"

    def run(self, name):
        return self.get_achievement_info(name)


class AdventurerRankWrapper:
    adventurer_ranks: list[AdventurerRank] = []

    def __init__(self, path="./resource/genshindb/adventureranks.json"):
        with open(path, 'r', encoding='utf-8') as file:
            adventurer_ranks_data = json.load(file)

        for data in adventurer_ranks_data:
            adventurer_rank = AdventurerRank(
                name=data['name'],
                exp=data.get('exp', 0),
                unlockdescription=data['unlockdescription'],
                reward=data.get('reward', []),
                version=data['version']
            )

            self.adventurer_ranks.append(adventurer_rank)

    def get_adventurer_rank_info(self, name):
        # 通过名字查询冒险等级信息
        for adventurer_rank in self.adventurer_ranks:
            if adventurer_rank.name == name:
                return adventurer_rank.get_message_chinese()
        return f"未找到名为'{name}'的冒险等级信息。"

    def run(self, name):
        return self.get_adventurer_rank_info(name)


class AnimalsWrapper:
    animals: list[Animal] = []

    def __init__(self, path="./resource/genshindb/animals.json"):
        with open(path, 'r', encoding='utf-8') as file:
            animals_data = json.load(file)

        for data in animals_data:
            animal = Animal(
                name=data['name'],
                description=data['description'],
                category=data['category'],
                counttype=data['counttype'],
                sortorder=data['sortorder'],
                images=data.get('images', {}),
                version=data['version']
            )

            self.animals.append(animal)

    def get_animal_info(self, name):
        # 通过名字查询动物信息
        for animal in self.animals:
            if animal.name == name:
                return animal.get_message_chinese()
        return f"未找到名为'{name}'的动物信息。"

    def run(self, name):
        return self.get_animal_info(name)


class ArtifactsWrapper:
    artifacts: list[Artifact] = []

    def __init__(self, path="./resource/genshindb/artifacts.json"):
        with open(path, 'r', encoding='utf-8') as file:
            artifacts_data = json.load(file)

        for data in artifacts_data:
            artifact = Artifact(
                name=data['name'],
                rarity=data['rarity'],
                set_bonus=data.get('set_bonus', {}),
                flower=data.get('flower', {})
            )

            self.artifacts.append(artifact)

    def get_artifact_info(self, name):
        # 通过名字查询圣遗物信息
        for artifact in self.artifacts:
            if artifact.name == name:
                return artifact.get_message_chinese()
        return f"未找到名为'{name}'的圣遗物信息。"

    def run(self, name):
        return self.get_artifact_info(name)


class ConstellationsWrapper:
    constellations: list[Constellation] = []

    def __init__(self, path="./resource/genshindb/constellations.json"):
        with open(path, 'r', encoding='utf-8') as file:
            constellations_data = json.load(file)

        for data in constellations_data:
            constellation = Constellation(
                name=data['name'],
                effect=data.get('effect', ''),  # 使用 get 方法，避免 KeyError
                images=data.get('images', {}),
                c1=data.get('c1', {}),
                c2=data.get('c2', {}),
                c3=data.get('c3', {}),
                c4=data.get('c4', {}),
                c5=data.get('c5', {}),
                c6=data.get('c6', {})
            )

            self.constellations.append(constellation)

    def get_constellation_info(self, name):
        # 通过名字查询命座信息
        for constellation in self.constellations:
            if constellation.name == name:
                return constellation.get_message_chinese()
        return f"未找到名为'{name}'的命座信息。"

    def run(self, name):
        return self.get_constellation_info(name)


class DomainsWrapper:
    domains: list[Domain] = []

    def __init__(self, path="./resource/genshindb/domains.json"):
        with open(path, 'r', encoding='utf-8') as file:
            domains_data = json.load(file)

        for data in domains_data:
            domain = Domain(
                name=data['name'],
                region=data['region'],
                domain_entrance=data['domainentrance'],
                domain_type=data['domaintype'],
                description=data['description'],
                recommended_level=data['recommendedlevel'],
                recommended_elements=data['recommendedelements'],
                unlock_rank=data['unlockrank'],
                reward_preview=data['rewardpreview'],
                disorder=data['disorder'],
                monster_list=data['monsterlist'],
                images=data.get('images', {}),
                version=data['version']
            )

            self.domains.append(domain)

    def run(self, name):
        for domain in self.domains:
            if domain.name == name:
                return domain.get_message_chinese()
        return f"未找到名为'{name}'的副本信息。"


class EnemiesWrapper:
    def __init__(self, path="./resource/genshindb/enemies.json"):
        self.enemies = []
        self.load_data(path)

    def load_data(self, path):
        with open(path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            for enemy_data in data:
                enemy = Enemies(enemy_data)
                self.enemies.append(enemy)

    def run(self, name):
        for enemy in self.enemies:
            if enemy.name == name:
                return enemy.get_message_chinese()
        return f"未找到名为'{name}'的敌人信息。"


class FoodWrapper:
    def __init__(self, path="./resource/genshindb/foods.json"):
        with open(path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        self.foods = [Food(item) for item in data]

    def run(self, name):
        for food in self.foods:
            if food.name == name or food.character == name:
                return food.get_message_chinese()
        return f"未找到名为'{name}'的食物信息。"


class GeographiesWrapper:

    def __init__(self, path="./resource/genshindb/geographies.json"):
        # 将json实例化为list
        with open(path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        self.geographies = [Geography(item) for item in data]

    def run(self, name):
        # 通过名字查询地理信息
        for geography in self.geographies:
            if geography.name == name or geography.area == name:
                return geography.get_message_chinese()
        return f"未找到名为'{name}'的地理信息。"


class MaterialsWrapper:
    def __init__(self, path="./resource/genshindb/materials.json"):
        with open(path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        self.materials = [Material(material_data) for material_data in data]

    def run(self, name):
        for material in self.materials:
            if material.name == name:
                return material.get_message_chinese()
        return f"未找到名为'{name}'的材料信息。"


class NameCardsWrapper:
    def __init__(self, path="./resource/genshindb/namecards.json"):
        self.namecards = []
        self.load_data(path)

    def load_data(self, path):
        with open(path, encoding='utf-8') as f:
            data = json.load(f)
            self.namecards = [NameCard(namecard_data) for namecard_data in data]

    def run(self, name):
        for namecard in self.namecards:
            if namecard.name == name:
                return namecard.get_message_chinese()
        return f"未找到名为'{name}'的名片信息。"


class OutfitsWrapper:
    def __init__(self, path="./resource/genshindb/outfits.json"):
        self.path = path
        self.outfits = self.load_outfits()

    def load_outfits(self):
        try:
            with open(self.path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                return [Outfit(outfit_data) for outfit_data in data]
        except FileNotFoundError:
            print(f"File not found: {self.path}")
            return []

    def get_outfit_by_name(self, name):
        for outfit in self.outfits:
            if outfit.name == name or outfit.character == name:
                return outfit
        return None

    def run(self, name):
        outfit_info = self.get_outfit_by_name(name)
        return outfit_info.get_message_chinese() if outfit_info else f"未找到名为'{name}'的装扮信息。"


class TalentsWrapper:
    def __init__(self, path="./resource/genshindb/talents.json"):
        self.talents = []
        self.load_data(path)

    def load_data(self, path):
        import json
        with open(path, "r", encoding="utf-8") as file:
            data = json.load(file)
        self.talents = [Talent(talent_data) for talent_data in data]

    def run(self, name):
        for talent in self.talents:
            result = talent.run(name)
            if result:
                return result
        return f"未找到名为'{name}'的天赋信息。"


class WeaponWrapper:
    weapons: list[Weapon] = []

    def __init__(self, path="./resource/genshindb/weapons.json"):
        # 将json实例化为list
        with open(path, 'r', encoding='utf-8') as file:
            weapon_data = json.load(file)

        for data in weapon_data:
            weapon = Weapon()
            weapon.name = data['name']
            weapon.description = data['description']
            weapon.weapontype = data['weapontype']
            weapon.rarity = data['rarity']
            weapon.story = data['story']
            weapon.baseatk = data['baseatk']
            weapon.substat = data['substat']
            weapon.subvalue = data['subvalue']
            weapon.effectname = data['effectname']
            weapon.effect = data['effect']
            weapon.r1 = data['r1']
            weapon.r2 = data['r2']
            weapon.r3 = data['r3']
            weapon.r4 = data['r4']
            weapon.r5 = data['r5']
            weapon.weaponmaterialtype = data['weaponmaterialtype']
            weapon.costs = data['costs']
            weapon.images = data['images']
            weapon.url = data.get('url', None)
            weapon.version = data['version']

            self.weapons.append(weapon)

    def run(self, name):
        # 通过名字查询武器信息
        for weapon in self.weapons:
            if weapon.name == name:
                return weapon.get_message_chinese()
        return f"未找到名为'{name}'的武器信息。"


class WindgliderWrapper:
    windgliders: list[Windglider] = []

    def __init__(self, path="./resource/genshindb/windgliders.json"):
        # 将json实例化为list
        with open(path, 'r', encoding='utf-8') as file:
            windglider_data = json.load(file)

        for data in windglider_data:
            windglider = Windglider()
            windglider.name = data['name']
            windglider.description = data['description']
            windglider.rarity = data['rarity']
            windglider.story = data['story']
            windglider.sortorder = data['sortorder']
            windglider.source = data['source']
            windglider.images = data['images']
            windglider.version = data['version']

            self.windgliders.append(windglider)

    def run(self, name):
        # 通过名字查询风之翼信息
        for windglider in self.windgliders:
            if windglider.name == name:
                return windglider.get_message_chinese()
        return f"未找到名为'{name}'的风之翼信息。"

    def query_windglider_info(self, name):
        for windglider in self.windgliders:
            if windglider.name == name:
                return windglider.description
        print(f"未找到名为'{name}'的风之翼信息。")


if __name__ == "__main__":
    # 示例使用
    character_match = CharacterWrapper("../resource/genshindb/characters.json")
    for character in character_match.characters:
        print(character.name, character.rarity, character.element, character.cv["english"])
    s = "钟离"
    info = character_match.query_character_info(s)
    print(info)
    wrapper = AchievementgroupsWrapper()

    # 打印所有成就组信息
    for group in wrapper.groups:
        print("成就组名：", group.name)
        print("排序编号：", group.sortorder)
        print("奖励信息：", group.reward)
        print("图片名称图标：", group.images['nameicon'])
        print("版本号：", group.version)
        print("\n")

    wrapper = AchievementsWrapper()

    # 打印所有成就信息
    for achievement in wrapper.achievements:
        print("成就名：", achievement.name)
        print("成就组：", achievement.achievementgroup)
        print("是否隐藏：", achievement.ishidden)
        print("排序编号：", achievement.sortorder)
        print("阶段数量：", achievement.stages)
        print("阶段1标题：", achievement.stage1.get('title', ''))
        print("阶段1描述：", achievement.stage1.get('description', ''))
        print("阶段1进度：", achievement.stage1.get('progress', 0))
        print("阶段1奖励：", achievement.stage1.get('reward', {}))
        print("版本号：", achievement.version)
        print("\n")
    achievement_info = wrapper.get_achievement_info("「…将一切希望弃扬。」")
    print(achievement_info)

    wrapper = AdventurerRankWrapper("../resource/genshindb")
    adventurer_rank_info = wrapper.run("59")
    print(adventurer_rank_info)

    wrapper = AnimalsWrapper("../resource/genshindb")
    animal_info = wrapper.run("长生仙")
    print(animal_info)

    wrapper = ArtifactsWrapper("../resource/genshindb")
    artifact_info = wrapper.run("冒险家")
    print(artifact_info)

    wrapper = ConstellationsWrapper("../resource/genshindb")
    constellation_info = wrapper.run("阿贝多")
    print(constellation_info)

    # 创建DomainsWrapper实例
    wrapper = DomainsWrapper("../resource/genshindb")

    # 查询副本信息
    domain_info = wrapper.run("祝圣秘境：椛狩 I")
    print(domain_info)

    # 查询不存在的副本信息
    non_existent_domain_info = wrapper.run("不存在的副本")
    print(non_existent_domain_info)

    # 查询敌人
    wrapper = EnemiesWrapper("../resource/genshindb")
    enemy_info = wrapper.run("深渊使徒·霜落")
    print(enemy_info)

    wrapper = FoodWrapper("../resource/genshindb")
    food_info = wrapper.run("阿如拌饭")
    print(food_info)

    # 初始化wrapper并查找特定地理信息
    wrapper = GeographiesWrapper("../resource/genshindb")
    geography_info = wrapper.run("赤王陵")
    print(geography_info)

    # Test the MaterialsWrapper
    wrapper = MaterialsWrapper("../resource/genshindb")
    material_info = wrapper.run("长生仙")
    print(material_info)

    # 示例测试
    wrapper = NameCardsWrapper("../resource/genshindb")
    namecard_info = wrapper.run("成就·强弓")
    print(namecard_info)

    wrapper = OutfitsWrapper("../resource/genshindb")
    outfit_info = wrapper.run("100%侦察骑士")
    print(outfit_info)

    # Example usage
    wrapper = TalentsWrapper("../resource/genshindb")
    talent_info = wrapper.run("阿贝多")
    print(talent_info)

    weapon_wrapper = WeaponWrapper("../resource/genshindb")
    description = weapon_wrapper.run("恶王丸")
    print(description)

    windglider_wrapper = WindgliderWrapper("../resource/genshindb")
    description = windglider_wrapper.run("苍天清风之翼")
    print(description)
