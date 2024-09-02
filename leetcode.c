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
