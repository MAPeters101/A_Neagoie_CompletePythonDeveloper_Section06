
class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print('run')
        return 'done'

player1 = PlayerCharacter('Cindy', 44)
player2 = PlayerCharacter('Tom', 21)
player2.attack = 50

print(player1)
print(player1.name)
print(player1.age)
#print(player1.attack)

print(player2)
print(player2.name)
print(player2.age)
print(player2.attack)

print()

print(player1.run)
print(player1.run())
