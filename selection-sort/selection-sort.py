
def selection_sort(array):

    for stp in range(len(array)):
        min_index = stp

        for j in range(stp+1, len(array)):

            if array[j] < array[min_index]:
                min_index = j

        array[stp], array[min_index] = array[min_index], array[stp]

    return array


