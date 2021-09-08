def gcd(a, b):
    # Everything divides 0
    if (b == 0):
        return a
    return gcd(b, a % b)

# Driver program to test above function
a = int(input("Enter the value of a:"))
b = int(input("Enter the value of b:"))
try:
    if (gcd(a, b) and b!=0):
        print('GCD of', a, 'and', b, 'is', gcd(a, b))
    else:
        print('Dividedbyzero exception')
except:
    print('not found')