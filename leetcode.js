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

// valid palindrome
 function isAlphanumeric(char) {
    return /^[a-z0-9]+$/i.test(char);
}

var isPalindrome = function(s) {
    var left = 0;
    var right = s.length - 1;

    while (left < right) {
        if (!isAlphanumeric(s[left])) {
            left += 1;
        } 
        else if (!isAlphanumeric(s[right])) {
            right -= 1;
        } 
        else if (s[left].toLowerCase() === s[right].toLowerCase()) {
            left += 1;
            right -= 1;
        } 
        else {
            return false;
        }
    }
    return true;
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

// heapsort
var swap = function(arr, i, j) {
    [arr[i], arr[j]] = [arr[j], arr[i]]
};

var build_heap = function(arr, n, i) {
    let largest = i;
    let left = 2*i + 1;
    let right = 2*i + 2;
    
    if (left < n && arr[left] > arr[largest]) {
        largest = left;
    };

    if (right < n && arr[right] > arr[largest]) {
        largest = right;
    };

    if (largest != i) {
        swap(arr, i, largest);
        build_heap(arr, n, largest);
    };
};

var heapsort = function(arr) {
    let n = arr.length;
    for (let i = Math.floor(n/2) - 1; i >= 0; i--) {
        build_heap(arr, n, i);
    };

    for (let i = n - 1; i > 0; i--) {
        swap(arr, i, 0);
        build_heap(arr, i, 0);
    };
};

// quicksort
var partition = function(arr, current_index, pivot) {
    let swap_marker = current_index - 1;
    for (let i = current_index; i < pivot; i++) {
        if (arr[i] <= arr[pivot]) {
            swap_marker++;
            if (i > swap_marker) {
                [arr[i], arr[swap_marker]] = [arr[swap_marker], arr[i]];
            }
        }
    }
    [arr[swap_marker + 1], arr[pivot]] = [arr[pivot], arr[swap_marker + 1]];
    return swap_marker + 1;
}

var quicksort = function(arr, left=0, right=null) {
    if (right === null) {
        right = arr.length - 1;
    }
    if (left < right) {
        let pivot = partition(arr, left, right);
        quicksort(arr, left, pivot - 1);
        quicksort(arr, pivot + 1, right);

// maximum Depth of Binary Tree (recursive)
/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
var maxDepth = function(root) {
    if (!root) {
        return 0
    }
    return 1 + Math.max(maxDepth(root.left), (maxDepth(root.right)))
};
    }
}

// merge alternatively
var mergeAlternately = function(word1, word2) {
    let count = 0;
    let result = '';

    while (word1.length > count || word2.length > count) {
        if (word1.length > count) {
            result += word1[count];
        }

        if (word2.length > count) {
            result += word2[count];
        }
        count +=1;
    }
    return result;
};
