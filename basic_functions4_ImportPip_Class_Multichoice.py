
'''
pack = open("package.py", "a")
#pack.write("import random\ndef roll_dice(num):\n\treturn random.randint(1, num)")
#pack.write("\n\ndef pow(base, p): \n\tresult = 1\n\tfor inpow in range(p):\n\t\tresult *= base\n\treturn result")
pack.close()
'''
import package
print(package.roll_dice(20))

#https://docs.python.org/3/py-modindex.html
#We can distinguish if a module is external module (in the web) by clicking in it and check if there's a path like "Source Code:Lib/xxx.py"
'''
# Chances are the modules you want to create is written by third-party

think: where are the modules listed in official website stored? 
build-in module
external module---in the Lib folder
'''

# go to cmd and use command "pip --version" to check if pip is installed, then we can start using command like "pip install ..."
# its location is at Lib/site-packages
# or use "pip uninstall ..." to uninstall it

'''
# This part should be in another script (ex: student.py)
class studenttt:
    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation
'''

from student import studenttt

student1 = studenttt("Jim", "Business", 3.1, False)
student2 = studenttt("Paul", "History", 2.5, True)
print(student2.gpa)

question_prompts = [
    "What color are shuttlecocks?\n(A) white\n(B) black\n(C) yellow\n"
    "What color is my mind on Monday?\n(A) red\n(B) blue\n(C) green\n"
    "What color are elephants?\n(A) purple\n(B) brown\n(C) grey\n"
]