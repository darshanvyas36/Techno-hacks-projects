import random
length = int(input("Enter length of password : "))

password = ['1','2','3','4','5','6','7','8','9','0','a','b','c','d','e','f','g','h','i','j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', "v", 'w', 'x', 'y', 'z', '@', '#', '$', '%', '*', '_', '!', " "]
result = ''
for i in range(length):
    result = result + random.choice(password)

print(result)