from bubble_sort.bubble_sort import bubble_sort
from insertion_sort.insertion_sort import insertion_sort
from quick_sort.quick_sort import quick_sort
from selection_sort.selection_sort import selection_sort
from two_pointers.two_pointers import two_pointers


if __name__ == "__main__":
    print("Hello, This is a CLI app for sorting items")
    algorithm = 0
    while True:
        print(
            """
please Choose one of the algorithm you want:
[1] bubble sort
[2] insertion sort
[3] quick sort
[4] selection sort
[5] two_pointers
[6] exit"""
)
        algorithm = input().strip()

        if algorithm == '6':
            break

        print("Please give me the array you want to sort which every element should be seperated by space: ")
        array = list(map(int, input().split()))

        if algorithm == '1':
            print("++++++++++++++++++ NOT SORTED ARRAY ++++++++++++++++++")
            print(array)
            print("++++++++++++++++++ SORTED ARRAY ++++++++++++++++++++++")
            print(bubble_sort(array))

        elif algorithm == '2':
            print("++++++++++++++++++ NOT SORTED ARRAY ++++++++++++++++++")
            print(array)
            print("++++++++++++++++++ SORTED ARRAY ++++++++++++++++++++++")
            print(insertion_sort(array))

        elif algorithm == '3':
            print("++++++++++++++++++ NOT SORTED ARRAY ++++++++++++++++++")
            print(array)
            print("++++++++++++++++++ SORTED ARRAY ++++++++++++++++++++++")
            print(quick_sort(array))

        elif algorithm == '4':
            print("++++++++++++++++++ NOT SORTED ARRAY ++++++++++++++++++")
            print(array)
            print("++++++++++++++++++ SORTED ARRAY ++++++++++++++++++++++")
            print(selection_sort(array))

        elif algorithm == '5':
            print("++++++++++++++++++ NOT SORTED ARRAY ++++++++++++++++++")
            print(array)
            print("++++++++++++++++++ SORTED ARRAY ++++++++++++++++++++++")
            print(two_pointers(array))
    print("Thanks for using me! \nGoodBye =)")


