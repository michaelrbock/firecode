// namespace std have been included for this problem.

// Add any helper functions(if needed) above.
int* selection_sort_array(int arr[], int size) {
    for (int i = 0; i < size - 1; ++i) {
        int min_index = i;
        for (int j = i + 1; j < size; ++j) {
            if (arr[j] < arr[min_index]) {
                min_index = j;
            }
        }
        // Swap min element into place.
        int temp = arr[i];
        arr[i] = arr[min_index];
        arr[min_index] = temp;
    }

    // Add your code above this line. Do not modify any other code.
    /* save the sorted array in int arr[] and return the same array */
    return arr;
}
