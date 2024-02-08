def add_one(some_list):

    value = int(''.join(map(str, some_list)))
    value += 1
    value_str = str(value)
    result_list = []
    for val in value_str:
        result_list.append(int(val))

    return result_list

assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")
