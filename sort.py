my_arr = [10, 8, 5, 12, 19];
min = my_arr[0];
for i in range(0, len(my_arr)):
    if (my_arr[i]<min):
        min = my_arr[i];
print("The smallest element in the array is:" +str(min));