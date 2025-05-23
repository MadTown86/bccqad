# Insertion - Sort Algorithm

# Pseudo Code:
# Input: An array A of n comparable elements
# Output: A sorted array
# For k from 1 to n-1 do insert A[k] into its proper location within A[0..k]

def insertion_sort(A):
    for k in range(1, len(A)):
        cur = A[k]
        j = k
        while j > 0 and A[j-1] > cur:
            A[j] = A[j-1]
            j -= 1
        A[j] = cur
    return A

# Test the insertion_sort function
if __name__ == "__main__":
    A = [5, 2, 9, 1, 5, 6]
    print("Original array:", A)
    sorted_A = insertion_sort(A)
    print("Sorted array:", sorted_A)