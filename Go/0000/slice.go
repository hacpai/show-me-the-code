package main

import "code.google.com/p/go-tour/pic"

func Pic(dx, dy int) [][]uint8 {
	ret := make([]([]uint8), dy)
	for i, _ := range ret {
		ret[i] = make([]uint8, dx)
		for j, _ := range ret[i] {
			ret[i][j] = uint8(i ^ j*i ^ j)
		}
	}
	return ret
}

func main() {
	pic.Show(Pic)
}
