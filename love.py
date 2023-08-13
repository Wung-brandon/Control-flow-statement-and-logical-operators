print('Welcome to Love Calculator')

name1 = input("What is your Name?:")
name2 = input("What is her Name?:")

combined_name = (name1 + name2).lower()

t = combined_name.count('t')
r = combined_name.count('r')
u = combined_name.count('u')
e = combined_name.count('e')

true = t + r + u + e

l = combined_name.count('l')
o = combined_name.count('o')
v = combined_name.count('v')
e = combined_name.count('e')

love = l + o + v + e

love_score = int(true + love)

if love_score < 10 or love_score > 90:
    print(f'Your love score is {love_score}, You go together like coke and mentos')
elif love_score >= 40 and love_score <= 50:
    print(f'Your love score is {love_score},You are alright together')
else:
    print(f'Your love score is {love_score}')




#def square(x):
 #   return x * x

#for i in range(10):
 #   print(f'the square of {i} is {square(i)}')