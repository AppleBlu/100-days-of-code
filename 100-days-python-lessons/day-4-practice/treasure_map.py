row1 = ["⬜️", "️⬜️", "️⬜️"]
row2 = ["⬜️", "⬜️", "️⬜️"]
row3 = ["⬜️️", "⬜️️", "⬜️️"]

new_map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to put the treasure? ")

position_x = int(position[0])
position_y = int(position[1])

new_map[position_y - 1][position_x - 1] = 'X'

print(f"{row1}\n{row2}\n{row3}")
