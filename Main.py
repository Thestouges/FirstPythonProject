from FindPrime import FindPrime
from WordFinder import WordFinder

print("1: Find prime up to number entered")
print("2: Find Word with inputted letters and length")
userinput = input("Enter Selection:")

if userinput == "1":
    num = input("Enter all prime number to max number: ")
    test = FindPrime()
    test.printPrime(int(num))

elif userinput == "2":
    numletters = input("Enter amount of letters: ")
    knownletters = input("Enter letters to search without spaces: ")
    findword = WordFinder(int(numletters), knownletters)
    findword.findworld()
    