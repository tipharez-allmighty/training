// Stream_processing package
package stream_processing

import (
	"fmt"
	"testing"
)

func TestKthLargest(t *testing.T) {
	kthLargest := Constructor(4, []int{4, 5, 8, 2})
	fmt.Println(kthLargest.nums)
	val := kthLargest.Add(4)
	fmt.Println(kthLargest.nums, val)
	fmt.Println(kthLargest.nums)
	val = kthLargest.Add(5)
	fmt.Println(kthLargest.nums, val)
}

func TestTrie(t *testing.T) {
	trie := NewTrie()
	trie.InsertReverse("something")
	fmt.Printf("%#v", trie)
}

func TestString(t *testing.T) {
	streamChecker := NewStreamChecker([]string{"abc", "xyz"})
	fmt.Printf("%#v", streamChecker)
	for _, val := range []byte{'a', 'b', 'c'} {
		fmt.Println(streamChecker.Query(val))
	}
}
