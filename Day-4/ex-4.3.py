"""The Treasure Map"""

row1 = ['🏴‍☠️','🏴‍☠️','🏴‍☠️']
row2 = ['🏴‍☠️','🏴‍☠️','🏴‍☠️']
row3 = ['🏴‍☠️','🏴‍☠️','🏴‍☠️']

map = [row1,row2,row3]

print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to place treasure ? ")
print(position[1])
row = map[int(position[1])-1]
row[int(position[0])-1] = '🪙'

print(f"{row1}\n{row2}\n{row3}")
