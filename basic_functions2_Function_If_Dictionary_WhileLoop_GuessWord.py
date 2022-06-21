def say_hi(name, IQ):
    print("Hello " + name + ", your IQ is " + str(IQ))
    print("test")

say_hi("Mike", "45")
say_hi("Sam", "negative")

def cube(num):
    return num*num*num
    print("This will not show up due to return")
print(cube(4))

def cube2(num):
    return num*num*num
Answer = cube2(5)
print(Answer)

'''
is_male = False
is_tall = False
if is_male or is_tall:
    print("You are tall or a male or both")
else:
    print("You are neither tall nor a male")

is_male = False
is_tall = True
if is_male and is_tall:
    print("You are a tall male")
elif is_male and not(is_tall):
    print("You are a short male")
elif not(is_male) and is_tall:
    print("You are a tall female")
else:
    print("You are a short female")
'''

#def find_max(n1, n2, n3):
#    if n1 >= n2 and n1 >= n3:
#        return n1
#    elif n2 >= n1 and n2 >= n3:
#        return n2
#    else:
#        return n3
#print(find_max(500, 500, 69))

#n1 = float(input("Enter the first number: "))
#op = input("Enter the operator: ")
#n2 = float(input("Enter the second number: "))

#if op == "+":
#    print(n1 + n2)
#elif op == "-":
#    print(n1 - n2)
#elif op == "*":
#    print(n1 * n2)
#elif op == "/":
#    print(n1 / n2)
#else:
#    print("Invalid operator")

'''
weekdic = {
    "0": "Monday",
    "Tue": "Tuesday",
    "Wed": "Wednesday",
    "Thu": "Thursday",
    "Fri": "Friday",
    "Sat": "Saturday",
    "Sun": "Sunday",
}

print("\n" + weekdic["0"])
print(weekdic.get("BBB"))
print(weekdic.get("BBB", "Invalid key"))
'''

#i = 1
#while i <= 10:
#    print("Before operating:" + str(i))
#    i += 2
#    print(i)
#print("Done with loop")

#answer = "one punch"
#guess = ""
#guess_count = 0
#guess_limit = 4
#while guess != answer and guess_count < guess_limit:
#    guess = (input("Enter your guess: "))
#    guess_count += 1

#if guess == answer:
#    print("You win!")
#else:
#    print("You lose! hohoho")

#for test in "Hero Academia":
#    print(test)
#friends = ["Nick", "Josh", "Ian", "Aaron"]
#for text in friends:
#    print(text)
#for index in range(len(friends)):
#    print(friends[index])
#for qqq in range(5):
#    print (qqq)
#for index in range(3,10):
#    print (index)
