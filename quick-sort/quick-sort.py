def quick_sort(array):

    if len(array) <= 1:
        return array

    pivot = array.pop()
    g_items = list()
    l_items = list()

    for item in array:
        if item > pivot:
            g_items.append(item)
        else:
            l_items.append(item)

    return quick_sort(l_items) + [pivot] + quick_sort(g_items)

