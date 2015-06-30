package main

import (
	"code.google.com/p/go-tour/wc"
	"strings"
)

func WordCount(sentence string) map[string]int {
	//hist := make(map[string] int)
	var hist map[string]int
	hist = make(map[string]int)
	for _, k := range strings.Fields(sentence) {
		hist[k]++
	}
	return hist
}

func main() {
	wc.Test(WordCount)
}
