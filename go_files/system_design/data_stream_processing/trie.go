package stream_processing

import "fmt"

type TrieNode struct {
	Children map[rune]*TrieNode
	End      bool
}

func NewTrieNode() *TrieNode {
	return &TrieNode{make(map[rune]*TrieNode, 26), false}
}

func (t *TrieNode) GoString() string {
	return fmt.Sprintf("TrieNode(Children: %#v, End: %v)", t.Children, t.End)
}

type Trie struct {
	Root *TrieNode
}

func NewTrie() *Trie {
	return &Trie{NewTrieNode()}
}

func (t *Trie) InsertReverse(word string) {
	current := t.Root
	runes := []rune(word)
	for i := len(runes) - 1; i >= 0; i-- {
		currentRune := runes[i]
		if _, ok := current.Children[currentRune]; !ok {
			current.Children[currentRune] = NewTrieNode()
		}
		current = current.Children[currentRune]
	}
	current.End = true
}

func (t *Trie) Search(word []rune) bool {
	current := t.Root

	for i := len(word) - 1; i >= 0; i-- {
		currenNode, ok := current.Children[word[i]]
		if !ok {
			return false
		}
		current = currenNode
		if current.End {
			return true
		}
	}
	return false
}
