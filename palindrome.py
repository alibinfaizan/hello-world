x = input('Enter string : ').upper()
x_reversed = x[::-1]

if x==x_reversed:
    print('The string is palindrome')
else:
    print('The string is not palindrome')
