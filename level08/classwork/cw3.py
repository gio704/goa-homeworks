user_input = input("enter a word with 3 letter")

if len(user_input) != 3:
        print("enter a word with 3 letter")
else:
        is_palindrome = True
        for i in range(len(user_input) // 2):
            if user_input[i] != user_input[-(i + 1)]:
                is_palindrome = False
        print(is_palindrome)