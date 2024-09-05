// binary search
var search = function(nums, target) {
    low = 0;
    high = nums.length - 1;
    while (high>=low){
        mid = low + Math.floor((high - low)/2);
        if (nums[mid] == target){
            return mid;
        }
        if (target > nums[mid]){
            low = mid + 1;
        }
        if (target < nums[mid]){
            high = mid - 1
        }
    }
    return -1
};

// search insert
var searchInsert = function(nums, target) {
    low = 0;
    high = nums.length - 1;

    while (high >= low) {
        mid = low + Math.floor((high - low)/2);
        if (nums[mid] < target) {
            low = mid + 1;
        }
        else {
            high = mid - 1;
        }
    }
    return low;
};

// Search in Rotated Sorted Array
var search = function(nums, target) {
    low = 0;
    high = nums.length - 1;

    while (low <= high) {
        mid = low + Math.floor((high - low) / 2);

        if (nums[mid] == target) {
            return mid;
        }
        
        if (nums[low] <= nums[mid]) { 
            if (target < nums[low] || target > nums[mid]) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        } else {  
            if (target < nums[mid] || target > nums[high]) {
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
    }

    return -1;  
};

// bubble sore

var bubble_sort = function(nums) {
    size = nums.length;
    for (i = 0; i < size - 1; i++) {
        for (j = 0; j < size - 1 - i; j++) {
            if (nums[j] > nums[j + 1]) {
                [nums[j], nums[j + 1]] = [nums[j + 1], nums[j]];
            }
        }
    }
}
