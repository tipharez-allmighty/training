// Reverse String
var reverseString = function(s) {
    let p1 = 0;
    let p2 = s.length - 1;
    
    while (p1 < p2) {
        [s[p1], s[p2]] = [s[p2], s[p1]];
        p1 += 1;
        p2 -= 1;
    }
}



// Invert Binary Tree
var invertTree = function(root) {
  if (!root) {
    return null;
  } else {
    [root.right, root.left] = [root.left, root.right]
    invertTree(root.left)
    invertTree(root.right)
    return root;
  }  
};

// Has cycle
var hasCycle = function(head) {
    let slow = head;
    let fast = head;
    while (fast && fast.next) {
        slow = slow.next
        fast = fast.next.next
        if (slow === fast) {
            return true;
        }
    }
    return false;
};
// Best Time to Buy and Sell Stocks
var maxProfit = function(prices) {
    let minPrice = Infinity;
    let maxProfit = 0;

    for (let price of prices) {
        if (price < minPrice) {
            minPrice = price;
        }
        else {
            maxProfit = Math.max(maxProfit,
                price - minPrice
            )
        }
    }
    return maxProfit
};
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

// reverse linked list
var reverseList = function(head) {
    if (head === null || head.next === null) {
        return head
    };
    let current = head
    let previous = null
    while (current) {
        let temp_node = current.next
        current.next = previous
        previous = current
        current = temp_node
    };
    return previous;
};

// merge two sorted linked lists
var mergeTwoLists = function(list1, list2) {
    const dummy = new ListNode()
    let tail = dummy
    while (list1 && list2) {
        if (list1.val < list2.val) {
            tail.next = list1
            list1 = list1.next
        } else {
            tail.next = list2
            list2 = list2.next
        }
        tail = tail.next
    }
    const last_node = list1 || list2
    if (last_node) {
        tail.next = last_node
    }
    return dummy.next;
};
