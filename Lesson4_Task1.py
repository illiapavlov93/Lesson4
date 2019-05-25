def swap(target_list, item_index1, item_index2):
    a = target_list[item_index1]
    target_list[item_index1] = target_list[item_index2]
    target_list[item_index2] = a
    return list1


list1 = [1, 2, 3, 4, 5]
print(swap(list1, 3, 4))
