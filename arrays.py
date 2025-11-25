import array as arr
arr_num=arr.array("i",[1,3,5,3,7,9,3])
print(arr_num)
print("The number of times 3 is repeated in the list is", arr_num.count(3))
arr_num.reverse()
print(arr_num)