package main

import "code.google.com/p/go-tour/reader"

type MyReader struct{}

func (m MyReader) Read(b []byte) (n int, err error) {
	for i := range b {
		b[i] = 'A'
	}
	return len(b), nil
}

func main() {
	reader.Validate(MyReader{})
}
