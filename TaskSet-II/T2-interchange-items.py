def swap_items(list):
    first = list[0]
    last = list[len(list)-1]
    list[0], list[len(list)-1] = last, first
    print(list)


swap_items([23, 65, 19, 90])
