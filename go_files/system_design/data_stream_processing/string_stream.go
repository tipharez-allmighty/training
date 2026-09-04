package stream_processing

type StreamChecker struct {
	trie   *Trie
	stream []rune
	maxLen int
}

func NewStreamChecker(words []string) StreamChecker {
	trie := NewTrie()
	maxLen := 0
	for _, word := range words {
		trie.InsertReverse(word)
		wordRune := []rune(word)
		if len(wordRune) > maxLen {
			maxLen = len(wordRune)
		}
	}
	sc := StreamChecker{trie, make([]rune, 0, maxLen), maxLen}
	return sc
}

func (this *StreamChecker) Query(letter byte) bool {
	if len(this.stream) < this.maxLen {
		this.stream = append(this.stream, rune(letter))
	} else {
		copy(this.stream, this.stream[1:])
		this.stream[len(this.stream)-1] = rune(letter)
	}
	isSuffix := this.trie.Search(this.stream)
	return isSuffix
}
