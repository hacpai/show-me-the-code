package main

import (
	"fmt"
	"io/ioutil"
	"net"
	"os"
	"sync"
)

func send() {
	service := "10.77.109.166:1200"
	tcpAddr, err := net.ResolveTCPAddr("tcp4", service)
	checkError(err)
	conn, err := net.DialTCP("tcp", nil, tcpAddr)
	checkError(err)
	_, err = conn.Write([]byte("HEAD / HTTP/1.0\r\n\r\n"))
	checkError(err)
	result, err := ioutil.ReadAll(conn)
	checkError(err)
	fmt.Println(string(result))
}

func checkError(err error) {
	if err != nil {
		fmt.Fprintf(os.Stderr, "Fatal error: %s", err.Error())
	}
}

func main() {
	NumEl := 100000 // Number of times the external program is called
	NumCore := 40   // Number of available cores
	c := make(chan bool, NumCore-1)
	wg := new(sync.WaitGroup)
	wg.Add(NumEl) // Set the number of goroutines to (0 + NumEl)
	for i := 0; i < NumEl; i++ {
		go callProg(i, c, wg)
		c <- true // At the NumCoreth iteration, c is blocking
	}
	wg.Wait() // Wait for all the children to die
	close(c)
}

func callProg(i int, c chan bool, wg *sync.WaitGroup) {
	defer func() {
		<-c
		wg.Done() // Decrease the number of alive goroutines
	}()
	send()
}
