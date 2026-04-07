def particion(array, menor, mayor):
    pivote = array[mayor]
    i = menor - 1
    for j in range(menor, mayor):
        if array[j] <= pivote:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[mayor] = array[mayor], array[i + 1]
    return i + 1
def quickSort(array, menor, mayor):
    if menor < mayor:
        p = particion(array, menor, mayor)
        quickSort(array, menor, p - 1)
        quickSort(array, p + 1, mayor)

array = [1, 7, 4, 1, 10, 9, -2]
quickSort(array, 0, len(array) - 1)
print(array)
