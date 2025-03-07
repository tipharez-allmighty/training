// bubble sort
void bubble_sort(int arr[], int size) {
    for (int i = 0; i < size - 1; i++) {
        for (int j = 0; j < size - 1 - i; j++) {
            if (arr[j] > arr[j+1]) {
                int temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
    }
}

// insert sort
void insert_sort(int arr[], int size) {
    for (int i = 0; i < size; i++) {
        int j = i;

        while (j > 0 && arr[j - 1] > arr[j]) {
            int temp = arr[j];
            arr[j] = arr[j - 1];
            arr[j - 1] = temp;
            
            j--;

        }
    }
}

// heapsort
void swap(int arr[], int i, int j);

void swap(int arr[], int i, int j) {
    int temp = arr[i];
    arr[i] = arr[j];
    arr[j] = temp;
};

void build_heap(int arr[], int size, int i);

void build_heap(int arr[], int size, int i) {
    int largest = i;
    int right = 2*i + 1;
    int left = 2*i + 2;
    
    if (left < size && arr[left] > arr[largest]) {
        largest = left;
    };

    if (right < size && arr[right] > arr[largest]) {
        largest = right;
    };

    if (largest != i) {
        swap(arr, largest, i);
        build_heap(arr, size, largest);
    };
    
};

void heapsort(int arr[], int size);

void heapsort(int arr[], int size) {
    for (int i = size/2 - 1; i >= 0; i--) {
        build_heap(arr, size, i);
    };

    for (int i = size - 1; i > 0; i--) {
        swap(arr, i, 0);
        build_heap(arr, i, 0);
    };
};

// quicksort
void swap(int arr[], int i, int j);

void swap(int arr[], int i, int j) {
    int temp = arr[i];
    arr[i] = arr[j];
    arr[j] = temp;
};

int partition(int arr[], int current_index, int pivot);

int partition(int arr[], int current_index, int pivot) {
    int swap_marker = current_index - 1;
    for (int i = current_index; i < pivot; i++) {
        if (arr[i] <= arr[pivot]) {
            swap_marker++;
            if (i > swap_marker) {
                swap(arr, i, swap_marker);
            }
        }
    }
    swap(arr, swap_marker + 1, pivot);
    return swap_marker + 1;
};

void quicksort(int arr[], int left, int right) {
    if (left < right) {
        int pivot = partition(arr, left, right);
        quicksort(arr, left, pivot - 1);
        quicksort(arr, pivot + 1, right);
    }
};
