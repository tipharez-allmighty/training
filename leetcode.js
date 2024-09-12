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

// insert sort
var insert_sort = function(nums) {
    for (i = 0; i < nums.length; i++) {
        j = i;

        while (j > 0 && nums[j - 1] > nums[j]) {
            [nums[j - 1], nums[j]] = [nums[j], nums[j - 1]];
            j--;
        }
    }
}

// recursive insert sort
var insert_sort_rec = function(nums, n=null) {
    if (n === null) {
        n = nums.length;
    }

    if (n <= 1) {
        return nums;
    }
    insert_sort_rec(nums, n-1);
    last = nums[n-1];
    j = n - 2;

    while (nums[j] > last && j >= 0) {
        nums[j+1] = nums[j];
        j = j - 1;
    }
    nums[j+1] = last;
}

// merge_sort
var merge_inner = function(arr1, arr2) {
    let temp_arr = []

    while (arr1.length != 0 && arr2.length != 0) {
        if (arr1[0] > arr2[0]) {
            temp_arr.push(arr2[0]);
            arr2.splice(0,1);
        }

        else {
            temp_arr.push(arr1[0]);
            arr1.splice(0,1);  
        }
    }
        while (arr1.length != 0) {
            temp_arr.push(arr1[0]);
            arr1.splice(0,1);
        }

        while (arr2.length != 0) {
            temp_arr.push(arr2[0]);
            arr2.splice(0,1);
        }        
    
        return temp_arr;
}

var merge_sort = function(arr) {
    let middle = arr.length / 2;
    let arr1 = arr.slice(0, middle);
    let arr2 = arr.slice(middle);

    if (arr.length == 1) {
        return arr;
    }

    arr1 = merge_sort(arr1);
    arr2 = merge_sort(arr2);
    
    return merge_inner(arr1, arr2);
}
