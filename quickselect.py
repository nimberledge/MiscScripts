# Author: Akhil Krishna Mohan
import random
import time
import matplotlib.pyplot as plt

def partition(arr, left, right, piv):
    '''Helper for select'''
    piv_val = arr[piv]
    arr[piv], arr[right] = arr[right], arr[piv]
    store = left
    for i in range(left, right):
        if arr[i] < piv_val:
            arr[store], arr[i] = arr[i], arr[store]
            store += 1
    arr[right], arr[store] = arr[store], arr[right]
    return store

def select(arr, left, right, k):
    '''Selects the k-th smallest element from an array'''
    if left == right:
        return arr[left]
    piv = left
    piv = partition(arr, left, right, piv)
    if k == piv:
        return arr[k]
    if k < piv:
        return select(arr, left, piv-1, k)
    return select(arr, piv+1, right, k)

def quickselect(arr, k):
    '''Wrapper function for select'''
    return select(arr, 0, len(arr)-1, k)

def time_trial(arr, k, x_points, y_points):
    start = time.time()
    c = quickselect(arr, k)
    t = time.time() - start
    print ("Result %d Time taken: %f" % (c, t))
    x_points.append(k)
    y_points.append(t)

def main():
    array_size = 100000
    arr = [i**2 for i in range(array_size)]
    random.shuffle(arr)
    temp_k = 4
    print ("Array size: ", array_size)
    x_pts = []
    y_pts = []
    for i in range(10):
        time_trial (arr, temp_k, x_pts, y_pts)
        temp_k *= 2
    plt.title('Quick select on array of size: ' + str(array_size))
    plt.xlabel('k-value')
    plt.ylabel('Execution time (s)')
    plt.plot(x_pts, y_pts)
    plt.show()

if __name__ == '__main__':
    main()
