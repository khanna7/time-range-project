

def timerange_to_minutes(t_str):
    """
    Convert format HH:MM to minutes
    : param t_str:
    :return:
    """

    #05:00
    hour = int (t_str.split(":")[0])
    minutes = int (t_str.split(":")[1])
    hours_to_minutes = hour*60

    return hours_to_minutes + minutes


def prettify_available_minutes():
    l = [0, 1, 2, 35, 46, 47, 60, 61, 62]
    grouped_list = [] #nested list
    list_resettable = []

    for element in l:
        if list_resettable == []:
            list_resettable.append(element)
            continue

        if list_resettable[-1] + 1 == element:
            list_resettable.append(element)

        else:
            grouped_list.append(list_resettable[:])
            list_resettable.clear()
            list_resettable.append(element)

        if list_resettable: #equivalent to if len(list_resettable) > 0, i.e., checking that list is non-empty
            grouped_list.append(list_resettable)


    print(grouped_list)


prettify_available_minutes()