// bubble sort
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
        
// count sort
var count_search = function(nums, k) {
    let counts = new Array(k).fill(0);
    let result = new Array(nums.length).fill(0);

    for (const num of nums) {
        counts[num]++; 
    };

    for (let i = 1; i < counts.length; i++) {
        counts[i] = counts[i-1] + counts[i];
    };
    
    for (let i = nums.length - 1; i>-1; i--) {
        let value = nums[i];
        let result_position = counts[value] - 1;
        result[result_position] = value;
        counts[value]--;
    };

    return result;
}
        
