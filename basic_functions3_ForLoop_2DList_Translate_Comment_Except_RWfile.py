#print(2**3)

def pppower(basic, power):
    result = 1
    for inpow in range(power):
        result *= basic
    return result

#print(pppower(2,4))

'''
td_list = [
    [1, 2, 3],
    [4, 5, 6, 7],
    [8, 9, 0],
    [1, 2],
    [3, 4, 5, 6, 7]
]

print(td_list[0][1])

for row in td_list:
    for col in row:
        print(col)
'''

'''
This comment form is not official

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
            #if letter in "AEIOU":
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation
print(translate(input("Enter a sentence: ")))
'''

'''
try:
    answer = 10/0
    number = int(input("Enter a number: "))
    print(number)
#except ZeroDivisionError:
except ZeroDivisionError as errr:
    print(errr)
except ValueError:
    print("Invalid value")
'''

'''
#open("game_list.txt", "r")
#open("game_list.txt", "w")
#open("game_list.txt", "a") means append (cannot modify, but can add things in it)
#open("game_list.txt", "r+w")

game_file = open("game_list.txt", "r")
#print(game_file.readable())
#print(game_file.read())
#print(game_file.readline())
#print(game_file.readline())
#print(game_file.readlines())
#print(game_file.readlines()[1])
for game in game_file.readlines():
    print(game)
game_file.close()
'''

'''
game_file = open("game_list.txt", "a")
game_file.write("\nConcordia")

# if game_list1.txt doesn't exist yet, it will be created in the same file as main.py
board_game = open("game_list1.txt", "w")
board_game.write("\nCubirds")

web = open("index.html", "a")
web.write("<p>This is a paragraph</p>")

game_file.close()
board_game.close()
web.close()
'''
