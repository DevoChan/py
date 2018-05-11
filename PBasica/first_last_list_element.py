def first_last(list_):
    new_list = []
    new_list.append(list_[0])
    new_list.append(list_[len(list_)-1])
    return new_list

arr = input("Enter a list: ")
print (first_last(arr))