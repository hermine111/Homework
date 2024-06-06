# 1.Write a Python function to sum all the numbers in a list.Sample List : (8, 2, 3, 0,
# 7)Expected Output : 20

def list_sum(list_ex):           # [4,5,8,7]
    result = 0
    for num in list_ex:
        result += num
    return result
print(list_sum([1,5,5, 8,7]))



