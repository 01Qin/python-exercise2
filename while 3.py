number = []
while number == "":
    number = input("enter a number:")
    break
if number:
    smallest = min(number)
    largest = max(number)
    print("the smallest number is:", smallest)
    print("the largest number is:", largest)
else:
    print("Execution stopped.")
