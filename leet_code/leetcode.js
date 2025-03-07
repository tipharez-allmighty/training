// Greatest Common Divisor of Strings
var gcdOfStrings = function(str1, str2) {
    for (let i=Math.min(str1.length, str2.length); i>0; i--) {
        if (str1.length % i === 0 && str2.length % i === 0) {
            n1 = str1.length / i;
            n2 = str2.length / i;
            base = str1.slice(0,i)
            if (str1 === base.repeat(n1) && str2 === base.repeat(n2)) {
                return base;
            }
        return '';
        }
    }
};

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
