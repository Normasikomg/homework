a = input()
def pal(x):
    x = a[::-1]
    if a == x:
        print("PALINDROM")
    else:
        print("not palindrom")
pal(a)