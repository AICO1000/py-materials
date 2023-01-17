def check_sum(num_list):
    check = 0
    found = False
    for n1 in num_list:
        for n2 in num_list:
            if n1 != n2:
                if n1 + n2 == check:
                    found = True
                    break
                
    if found:
        return check == 0
    else:
        return check != 0
lst = [10, -14, 26,-3, 13, -5, 5]


print(check_sum(lst))


'''def check_sum(num_list):
    for first_num in range(len(num_list)):
        for second_num in range(first_num + 1, len(num_list)):
            if num_list[first_num] + num_list[second_num] == 0:
                return True
    return False


num_list = [10, -14, 26, 5, -3, 13, -5]
print(check_sum(num_list))
'''