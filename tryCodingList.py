'''
Exercise to write the sorted list myself

Sort list =10, 11, 12, 45, 60, 61, 62, 69 in groups of 
consecutive values, such as

sorted_list = [[10, 11, 12], [45], [60, 61, 62], [69]]
'''

def create_sorted_list():
    l = [10, 11, 12, 45, 60, 61, 62, 69]
    big_list = []
    small_list = []

    #print(range(len(l)))

    for e in l:
       if not small_list or small_list[-1] + 1 == e:
           small_list.append(e)
       
       elif small_list[-1] + 1 != e:
           big_list.append(small_list[:])
           small_list = [e]

    if small_list:
            big_list.append(small_list[:])

    print(small_list)
    print(big_list)


create_sorted_list()