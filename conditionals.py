"""
for i in range(1, 13):
    print("The number is ")

age = int(input("Enter your age "))

if age >= 18: 
    print("You can vote")
elif age == 1000:
    print("Dude you already pass away!................")
else:
    print("Please come back in {0} years" .format(18 - age))
"""
print("-" * 50)
    
guess = int(input("Please Enter a Number: "))
for i in range(1, 10):
    if(i == guess):
        print("Your guess number is: ", i)
        
