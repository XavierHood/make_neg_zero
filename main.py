numbers = [5, -1, 6, -1, 9]
# numbers[2] = 20
# print(numbers)


index = 0
for number in numbers:
    if number < 0:
        numbers[index] = 0
    index += 1

print(numbers)