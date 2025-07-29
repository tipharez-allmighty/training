class Heap {
    constructor(arr) {
        this.arr = arr || [];
    }

    length() {
        return this.arr.length;
    }

    swap(i, j) {
        [this.arr[i], this.arr[j]] = [this.arr[j], this.arr[i]]
    }

    buildHeap(n, i) {
        let parent = i;
        let left = 2*i + 1;
        let right = 2*i + 2;

        if (left < n && this.arr[parent] < this.arr[left]) {
            parent = left;
        }
        if (right < n && this.arr[parent] < this.arr[right]) {
            parent = right;
        }
        if (parent !== i) {
            this.swap(parent, i);
            this.buildHeap(n, parent)
        }
    }

    heapify(n=null) {
        if (!n) {
            n = this.arr.length
        }
        let i = Math.floor(n / 2) - 1;

        for (let j = i; j >= 0; j--) {
            this.buildHeap(n, j);
        }
    }

    bubbleUp(node=null) {
        if (!node) {
            node = this.arr.length - 1
        }
        let parent = Math.floor((node - 1) / 2)
        while (node !== 0 && this.arr[node] > this.arr[parent]) {
            this.swap(node, parent)
            node = parent
            parent = Math.floor((node - 1) / 2)
        }
    }

    bubbleDown(node=null) {
        let n = this.length();
        if (!node) {
            node = 0;
        }
        while (true){
            let left = 2*node + 1;
            let right = 2*node + 2;
            let largest = node;
            if (left < n && this.arr[largest] < this.arr[left]) {
                largest = left;
            }
            if (right < n && this.arr[largest] < this.arr[right]) {
                largest = right;
            }
            if (largest !== node) {
                this.swap(node, largest)
                node = largest;
            } else {
                break
            }
        }
        }
    heapPush(element) {
        this.arr.push(element);
        this.bubbleUp();
    }

    heapPop() {
        this.swap(0, this.length() - 1)
        let maxValue = this.arr.pop();
        this.bubbleDown();
        return maxValue;
    }
}
