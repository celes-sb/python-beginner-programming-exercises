# Your code here!!
def sing():
    result = " "
    for lyric in range(10):
        if lyric == 4:
            result += "whisper words of wisdom, "
        elif lyric == 9:
            result += "there will be an answer, let it be "
        else:
            result += "let it be, "
    return result

print(sing())