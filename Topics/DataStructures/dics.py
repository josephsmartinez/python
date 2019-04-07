phone = {
    "Phone 1": 100 ,
    "Phone 2": 232,
    "Phone 3": 435,
    "Phone 4": 545,
    "Phone 5": 323,
    "Phone 6": 124,
    "Phone 7": 125
}

print(type(phone))
print(phone["Phone 1"])

phone["Phone 1"] = 1000

print(phone["Phone 1"])

for k,v in phone.items():
    print( str(k) +" "+ str(v))


# Simple exercise
capitals = {}
capitals["USA"] = "Washington"
capitals["Jordan"] = "Amman"
capitals["Brazil"] = "Brasilia"

print(len(capitals))

coutries = ["USA", "France", "Russia", "Japan", "China", "South Africa"]

print(type(capitals))
print(type(coutries))
print(coutries)

for i in coutries:
    print(i)
    if i in capitals:
        print(i, capitals[i])
    else:
        print("Unknown")

print("-----------------")

x = 1
fact = 4
for i in range(1,fact+1):
    if i > 0:
        x = x * i
print("Factoral of " + str(fact) + " = " + str(x))

# Recursive function for factoral
def factoral(value):
    if value <= 0:
        return 1
    else:
        return value * factoral(value -1 )

print("Factoral using recursion: ", factoral(4))