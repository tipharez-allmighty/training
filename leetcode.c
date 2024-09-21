// binary search
int search(int* nums, int numsSize, int target) {
    int low = 0;
    int high = numsSize - 1;
    
    while (high>=low){
        int mid = low + (high - low)/2;

        if (nums[mid] == target) {
            return mid;
        }
        if (nums[mid] > target) {
            high = mid - 1;
        }
        else {
            low = mid + 1;
        }
    }
    return -1;
}

// search insert
int searchInsert(int* nums, int numsSize, int target) {
    int low = 0;
    int high = numsSize - 1;

    while (high >= low) {
        int mid = low + (high - low)/2;

        if (nums[mid] < target) {
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }
    return low;
}

//Search in Rotated Sorted Array
int search(int* nums, int numsSize, int target) {
  int low = 0;
  int high = numsSize - 1;

  while (low <= high) {
    int mid = low + (high - low)/2;
    
    if (nums[mid] == target) {
        return mid;
    }
    if (nums[mid] >= nums[low]) {
        if (target < nums[low] || target > nums[mid]) {
            low = mid + 1;
        }
        else {
            high = mid - 1;
        }
    }

    else {
        if (target > nums[high] || target < nums[mid]) {
            high = mid - 1;
        }
        else {
            low = mid + 1;
        }
    }
  }
  return -1;  
}

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
