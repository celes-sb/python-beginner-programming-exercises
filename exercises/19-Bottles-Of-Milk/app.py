# Your code here!
def number_of_bottles():
    song = " "
    for bottle in range(100, 0, -1):
        if bottle in range(3, 100):
            song += f'{bottle} bottles of milk on the wall, {bottle} bottles of milk.\nTake one down and pass it around, {bottle - 1} bottles of milk on the wall.\n\n'
        elif bottle == 2:
            song += f'2 bottles of milk on the wall, 2 bottles of milk.\nTake one down and pass it around, 1 bottle of milk on the wall.\n\n'
        elif bottle == 1:
            song += '1 bottle of milk on the wall, 1 bottle of milk.\nTake one down and pass it around, no more bottles of milk on the wall.\n\n'
        elif bottle == 0:
            song += 'No more bottles of milk on the wall, no more bottles of milk.\nGo to the store and buy some more, 99 bottles of milk on the wall.\n\n'
    return song

print(number_of_bottles())