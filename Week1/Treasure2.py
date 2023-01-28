row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
# assumes the user will enter : which column then which row
position = input("Where do you want to put the treasure? ")
# let i be the first index (which nested list)
# let j be the index of the element in that nested list
j = int(position[0])-1
i = int(position[1])-1

map[i][j] = 'X'

print(f"{row1}\n{row2}\n{row3}")