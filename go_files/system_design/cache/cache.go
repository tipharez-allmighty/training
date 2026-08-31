// Package cache
package cache

import (
	"container/list"
)

type LRUCache struct {
	cache    map[int]*list.Element
	llist    *list.List
	capacity int
}

type Pair struct {
	key int
	val int
}

func ConstructorLRU(capacity int) LRUCache {
	return LRUCache{cache: make(map[int]*list.Element, capacity), llist: list.New(), capacity: capacity}
}

func (this *LRUCache) Get(key int) int {
	if element, ok := this.cache[key]; !ok {
		return -1
	} else {
		pair, ok := element.Value.(Pair)
		if !ok {
			return -1
		}
		this.llist.MoveToBack(element)
		return pair.val
	}
}

func (this *LRUCache) Put(key int, value int) {
	if element, ok := this.cache[key]; ok {
		element.Value = Pair{key: key, val: value}
		this.llist.MoveToBack(element)
		return
	}
	if len(this.cache) == this.capacity {
		element := this.llist.Front()
		evictElement := element.Value.(Pair)
		delete(this.cache, evictElement.key)
		this.llist.Remove(element)
	}
	element := this.llist.PushBack(Pair{key: key, val: value})
	this.cache[key] = element
}

type LFUCache struct {
	cache    map[int]*list.Element
	freq     map[int]*list.List
	minFreq  int
	capacity int
}

type PairFreq struct {
	Pair
	freq int
}

func ConstructorLFU(capacity int) LFUCache {
	return LFUCache{cache: make(map[int]*list.Element, capacity), freq: make(map[int]*list.List), capacity: capacity}
}

func (this *LFUCache) Get(key int) int {
	element, ok := this.cache[key]
	if !ok {
		return -1
	}
	pairFreq, ok := element.Value.(PairFreq)
	if !ok {
		return -1
	}
	oldElemList, ok := this.freq[pairFreq.freq]
	if ok {
		oldElemList.Remove(element)
		if oldElemList.Len() == 0 {
			delete(this.freq, pairFreq.freq)
			if pairFreq.freq == this.minFreq {
				this.minFreq++
			}
		}
	}
	delete(this.cache, key)
	pairFreq.freq++
	llist, ok := this.freq[pairFreq.freq]
	if !ok {
		llist = list.New()
		this.freq[pairFreq.freq] = llist
	}
	newElement := llist.PushBack(PairFreq{Pair: pairFreq.Pair, freq: pairFreq.freq})
	this.cache[key] = newElement
	return pairFreq.val
}

func (this *LFUCache) Put(key int, value int) {
	if element, ok := this.cache[key]; ok {
		oldPair := element.Value.(PairFreq)
		oldElemList, ok := this.freq[oldPair.freq]
		if ok {
			oldElemList.Remove(element)
			if oldElemList.Len() == 0 {
				delete(this.freq, oldPair.freq)
				if oldPair.freq == this.minFreq {
					this.minFreq++
				}
			}
		}
		newPair := oldPair
		newPair.val = value
		newPair.freq++
		newElemList, ok := this.freq[newPair.freq]
		if !ok {
			newElemList = list.New()
			this.freq[newPair.freq] = newElemList
		}
		element := newElemList.PushBack(PairFreq{Pair: Pair{key: key, val: value}, freq: newPair.freq})
		this.cache[key] = element
		return
	}
	if len(this.cache) == this.capacity {
		lfulist := this.freq[this.minFreq]
		element := lfulist.Front()
		evictElement := element.Value.(PairFreq)
		delete(this.cache, evictElement.key)
		lfulist.Remove(element)
		if lfulist.Len() == 0 {
			delete(this.freq, this.minFreq)
		}
	}
	newMinFreq := 1
	this.minFreq = newMinFreq
	newElemList, ok := this.freq[newMinFreq]
	if !ok {
		newElemList = list.New()
		this.freq[newMinFreq] = newElemList
	}
	element := newElemList.PushBack(PairFreq{Pair: Pair{key: key, val: value}, freq: newMinFreq})
	this.cache[key] = element
}
