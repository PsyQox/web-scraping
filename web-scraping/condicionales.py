from random import *
"""
>
<
>=
=<
==
|=
!=
&&
"""
x = randint(0, 10)
y = randint(0, 10)

print(x)
print(y)

print(x > y and x != y)
print(x < y)

if x == y:
    print("x is equal to y")
elif x > y:
    print("x is greater than y")
else:
    print("Don't into some condition")