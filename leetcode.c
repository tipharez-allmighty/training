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
int bubble_sort(int arr[], int size) {
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
