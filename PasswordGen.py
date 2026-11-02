
import random
import string
def main():

    
    length = intGetter("Enter the length of the password: ")
    CapMin=intGetter("Enter the minimum number of capital letters: ")
    LowMin=intGetter("Enter the minimum number of lowercase letters: ")
    SpecMin=intGetter("Enter the minimum number of special characters: ")
    
    print(generatePassword(CapMin, LowMin, SpecMin, length))

def generatePassword(CapMin=0, LowMin=0, SpecMin=0,length=0):
    if length < CapMin + LowMin + SpecMin:
        length = CapMin + LowMin + SpecMin
    password = ''
    CapCount = 0
    LowCount = 0
    SpecCount = 0
    while len(password) < length:
        charType = random.choice(['cap', 'low', 'spec'])
        if charType == 'cap' and CapCount < CapMin:
            password += random.choice(string.ascii_uppercase)
            CapCount += 1
        elif charType == 'low' and LowCount < LowMin:
            password += random.choice(string.ascii_lowercase)
            LowCount += 1
        elif charType == 'spec' and SpecCount < SpecMin:
            password += random.choice(string.punctuation)
            SpecCount += 1
        else:
            charType = random.choice(['cap', 'low', 'spec'])
            if charType == 'cap':
                password += random.choice(string.ascii_uppercase)
            elif charType == 'low':
                password += random.choice(string.ascii_lowercase)
            else:
                password += random.choice(string.punctuation)
    print(f"\n\tGenerated password: {password}")
    return password

def test1():    #standard test-should work
    return  testMaker(12, 2, 4, 2)

def test2():    # 1, 2, 1 #test with no length specified, should default to 4
    return testMaker(1, 2, 1)

def test3():    #16, 3, 5, 3
    return testMaker( 3, 5, 3, 16)

def testMaker( CapMin, LowMin, SpecMin, length=0):
    password = generatePassword(CapMin, LowMin, SpecMin, length)
    print(f"Test parameters: \n\
            length:{length} \n\
            CapMin:{CapMin} \n\
            LowMin: {LowMin} \n\
            SpecMin:{SpecMin}")
    # assert len(password) >= length
    # assert sum(1 for c in password if c.isupper()) >= CapMin
    # assert sum(1 for c in password if c.islower()) >= LowMin
    # assert sum(1 for c in password if not c.isalnum()) >= SpecMin
    print(f"Password statistics: \n\
            Password length: {len(password)} \n\
            Uppercase: {sum(1 for c in password if c.isupper())} \n\
            Lowercase: {sum(1 for c in password if c.islower())} \n\
            Special characters: {sum(1 for c in password if not c.isalnum())}")    
    return password

def shorter(password, type):
    return sum(1 for c in password if type(c))

def intGetter(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter an integer.")


main()


