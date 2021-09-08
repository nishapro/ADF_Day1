def decimalToBinary(n):
    if (n > 1):
        decimalToBinary(n // 2)
    print(n % 2, end='')

def decToOctal(n):
    octalNum = [0] * 100
    i = 0
    while (n != 0):
        octalNum[i] = n % 8
        n = int(n / 8)
        i += 1
    for j in range(i - 1, -1, -1):
        print(octalNum[j], end="")
def decToHexa(n):
	hexaDeciNum = ['0'] * 100
	i = 0
	while(n != 0):
		temp = 0
		temp = n % 16
		if(temp < 10):
			hexaDeciNum[i] = chr(temp + 48)
			i = i + 1
		else:
			hexaDeciNum[i] = chr(temp + 55)
			i = i + 1
		n = int(n / 16)
	j = i - 1
	while(j >= 0):
		print((hexaDeciNum[j]), end="")
		j = j - 1
n=int(input("Enter the value of n:"))
decimalToBinary(n)
print("\n")
decToOctal(n)
print("\n")
decToHexa(n)





