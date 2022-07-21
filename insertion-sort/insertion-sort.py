def insertion_sort(array):

    for i in range(1, len(array)):
        temp = array[i]
        pos = i - 1

        while pos >= 0:

            if array[pos] > temp:
                array[pos+1] = array[pos]
                pos -= 1
            else:
                break

        array[pos+1] = temp

    return array


