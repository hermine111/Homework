# 3.Write a python function, which create a dictionary
# for given number N, where keys are numbers from
# 1 to N, and values are cubes of that numbers


def cube_dict(n):
    my_dict = {}
    for i in range(1, n + 1):
        my_dict[i] = i**3
    return my_dict


print(cube_dict(8))
