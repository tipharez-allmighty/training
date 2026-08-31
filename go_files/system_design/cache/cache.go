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

func Constructor(capacity int) LRUCache {
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
