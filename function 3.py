numbers = []
while True:
    number = input("enter a number or input an empty string to quit: ")
    if number == "":
        break
    numbers.append(float(number))
sorted_numbers = sorted(numbers, reverse=True)
five_numbers = sorted_numbers[:5]
print("The five greatest numbers in descending order:")
for n in five_numbers:
    print(f"the five greatest number are {n}.")