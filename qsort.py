import random
def quicksort(A):
    if len(A) <= 1:
        return A

    pivot = A[0]
    left = [A[index] for index in range(1, len(A)) if A[index] <= pivot]
    right = [A[index] for index in range(1, len(A)) if A[index] > pivot]
    left = quicksort(left)
    right = quicksort(right)
    return left + [pivot] + right

if __name__ == '__main__':
    A = [random.randint(1, 10) for i in range(100)]
    A  = quicksort(A)
    print (A)
