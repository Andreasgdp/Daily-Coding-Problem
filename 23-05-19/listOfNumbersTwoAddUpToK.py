numbers = [10, 15, 3, 7]
target_number = 17

for i, number in enumerate(numbers[:-1]):  # note 1
    complementary = target_number - number
    if complementary in numbers[i+1:]:  # note 2
        print("Solution Found: {} and {}".format(number, complementary))
        break
else:  # note 3
    print("No solutions exist")
