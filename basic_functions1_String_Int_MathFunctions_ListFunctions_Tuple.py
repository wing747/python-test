# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


#def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
  #  print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
    #print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

f_name = "Joseph"
skill_name = "board games"

print("My friend is " + f_name + ",")
print("He is really good at " + skill_name + ".")

f_name = "William"
print("\nMy name is " + f_name + ",")
print("I'm also \"\"good\"\" at " + skill_name + '.')

phrase = "Hero Academia"
print("\n The string is: " + phrase)
print("It's upper-case string is: " + phrase.upper())
print(phrase.upper().isupper())
print("The first character is: " + phrase[0])
print(phrase.index("e"))
print("The index of first \'e\' is: " + str(phrase.index("e")))
print(phrase.index("Aca"))
print(phrase.replace("Hero","Badguy"))

test_num = -5
print(test_num)
print(abs(test_num))
print(pow(-5,3))
print(max(4,-8))
print(min(4,-8))
print(round(3.4))
print(round(3.7))
from math import *
print(floor(4.8))
print(ceil(4.8))
print(sqrt(36.23))

#name = input("Enter your name: ")
#print("Hello Moto! Just kidding, hello " + name + "!")


#num1 = input("Enter the first number: ")
#num2 = input("Enter the second number: ")
#result = float(num1) + float(num2)
#print(result)

#verb = input("Enter a verb: ")
#da_item = input("Enter the name of an item in your place: ")
#color = input("Enter a color: ")
#print("I love to " + verb + " others' " + da_item + ",")
#print("if it's in " + color + ", I would like to " + verb + " more.")

friends = ["Kyle", "Dale", "Joseph", 2, False, "Jimmy", "Walter", "Jessy"]
#print(friends)
#friends[1] = "Alex"
#print(friends[1:])
#print(friends[1:4])
emp_number = [4,7,8,13,25,26,29]
friends.extend(emp_number)
print(friends)
friends.append("Kim")
print(friends)
friends.insert(2,"Sammy")
print(friends)
friends.remove("Jimmy")
print(friends)
friends.clear()
print(friends)
friends = ["Kyle", "Dale", "Joseph", 2, False, "Jimmy", "Dale", "Walter", "Jessy"]
print(friends.index("Walter"))
print(friends.count("Dale"))
friends = ["Kyle", "Dale", "Joseph", "Jimmy", "Dale", "Walter", "Jessy"]
friends.sort()
print(friends)
friends.reverse()
print(friends)
friends2 = friends.copy()
print(friends2)

tuple = (4,5)
#elements in tuple cannot be assigned, but those in list can be
print(tuple[0])
uuu = [(7,5,5), (5,9,3), (3,4,5,5)]
print (uuu[2])

