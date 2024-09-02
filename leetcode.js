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
