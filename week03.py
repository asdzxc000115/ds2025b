#import array

#arr = array.array[11, 9, -77, 8]
#for i in range(len(array)):
#    print(f"{array[i]:3} {id(array[i])}")


#print(f"{array[0]:3} {id(array[0])}")
#print(f"{array[1]:3} {id(array[1])}")
#print(f"{array[2]:3} {id(array[2])}")
#print(f"{array[3]:3} {id(array[3])}")

def move_zeros(a_list):
    zero_index = 0
    for index, n in enumerate(a_list):
        if n != 0:
            a_list[zero_index] = n
            if zero_index != index:
                a_list[index] = 0
            zero_index += 1
        return(a_list)

a_list = [8, 0, 3, 0, 12]
move_zeros(a_list)
print(a_list)
