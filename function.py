# def even_odd(num):
#     if num % 2 == 0:
#         print ("Even number")
#     else:
#         print ("Odd number")

# print(even_odd(10))  

# age=int(input("Enter your age: "))
# if age >= 18:
#     print("You are eligible to vote")

# elif age < 18:
#     print("You are not eligible to vote")
# else:   
#     print("You are not eligible to vote")

def is_palindrome(word):
        return word == word[::-1]

def pailndrome_project():
    word = input("Enter a word:")
    if is_palindrome(word):
        print("yes,is a palindrome.")
    else:
        print("no is not a palindrome.")     

pailndrome_project()


    
    