package main

import "fmt"

func remove(slice []Type, elems ...Type) []Type {
	isInElems := make(map[Type]bool)
	for _, elem := range elems {
		isInElems[elem] = true
	}
	w := 0
	for _, elem := range slice {
		if !isInElems[elem] {
			slice[w] = elem
			w += 1
		}
	}
	return slice[:w]
}

func main() {
	urls := []string{"test", "abc", "def", "ghi"}
	urls = remove(urls, "abc", "test")
	fmt.Println(urls)
}
