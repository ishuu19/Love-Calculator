#Love calculator

Your_Name = input("What is your full name?").lower()
Partner_Name = input("What is your partner's full name?").lower()

T = Your_Name.count("t")+ Partner_Name.count('t')
R = Your_Name.count("r")+ Partner_Name.count('r')
U = Your_Name.count("u")+ Partner_Name.count('u')
E = Your_Name.count("e")+ Partner_Name.count('e')

true_count = T+R+U+E

L = Your_Name.count("l")+ Partner_Name.count('l')
O = Your_Name.count("o")+ Partner_Name.count('o')
V = Your_Name.count("v")+ Partner_Name.count('v')
E = Your_Name.count("e")+ Partner_Name.count('e')

love_count= (L+O+V+E)

your_score = int(f'{true_count}' + f'{love_count}')
print(f"Your love score is {your_score}")

if your_score<10 or your_score >=90:
    print('You can go together like coke and mentos!')
elif your_score >40 and your_score <=50:
    print('You are alright together.')