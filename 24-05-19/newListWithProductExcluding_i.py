start_list = [1, 2, 3, 4, 5]

product_array = []

for i in range(len(start_list)):  # note 1
    result = 1
    for j in range(len(start_list)):  # note 2
        if start_list[j] != start_list[i]:  # note 3
            result *= start_list[j]
    product_array.append(result)

print(product_array)
