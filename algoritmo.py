def particion(array, menor, mayor):
    pivote = array[mayor]
    i = menor - 1
    for j in range(menor, mayor):
        if array[j] <= pivote:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[mayor] = array[mayor], array[i + 1]
    return i + 1