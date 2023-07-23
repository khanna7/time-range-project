

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

def minutes_to_timerange_str(m):
    """
    (not the solution shown in the video)
    Return a timerange str in format HH:MM for a given integer
    :param m: integer representing minutes
    :return: formatted time string
    m = 90 -> 01:30 
    """
    hh, mm = divmod(m, 60)
    return f"{hh:02d}:{mm:02d}"



def prettify_available_minutes(l:list):

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

    if list_resettable:
        grouped_list.append(list_resettable)

    time_ranges = []
    for group in grouped_list:
        start_time = minutes_to_timerange_str(m=group[0])
        end_time = minutes_to_timerange_str(m=group[-1])
        time_range_str = f"{start_time} - {end_time}"
        time_ranges.append(time_range_str)

    return time_ranges


    


