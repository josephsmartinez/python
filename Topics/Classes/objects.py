class Elf():
    
    # constructor method
    # =None means the input params is not required
    def __init__(self, level, ability_scores=None):
        self.level = level
        self.ability_scores = {
            "str": 11,
            "dex": 12,
            "con": 10,
            "int": 16,
            "wis": 14,
            "cha": 13,
            "hel": 10
        }if ability_scores is None else ability_scores

        self.hp = 20 + self.ability_scores["hel"]

    def function1(self):
        pass

    @staticmethod
    def function2():
        pass

    @classmethod
    def function3(self):
        pass

# Here we'll build the classes and print
gregElf = Elf(1, {
            "str": 11,
            "dex": 12,
            "con": 10,
            "int": 16,
            "wis": 14,
            "cha": 13,
            "hel": 5
}
         )

print(gregElf)

joeElf = Elf(10, None)

print(joeElf)

print(joeElf.level, joeElf.ability_scores)

print(gregElf.hp, joeElf.hp)