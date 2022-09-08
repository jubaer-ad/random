import stringRev
s = input("Enter a string to check palindrome: ").lower()
if s.__eq__(stringRev.rev(s).lower()):
    print("It's palindrome!")
else:
    print("Owo! It's not palindrome!")