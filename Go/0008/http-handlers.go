package main

import (
	"fmt"
	"log"
	"net/http"
	"strings"
)

type String string

type Struct struct {
	Greeting string
	Punct    string
	Who      string
}

type Hello struct{}

func (s String) ServeHTTP(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "%s", s)
}

func (s *Struct) ServeHTTP(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "%s%s %s", s.Greeting, s.Punct, s.Who)
}

func (h Hello) ServeHTTP(w http.ResponseWriter, r *http.Request) {
	fmt.Fprint(w, "Welcome")
}

func sayhelloName(w http.ResponseWriter, r *http.Request) {
	r.ParseForm()
	fmt.Println(r.Form)
	fmt.Println("paht", r.URL.Path)
	fmt.Println("Scheme", r.URL.Scheme)
	fmt.Println(r.Form["url_long"])
	for k, v := range r.Form {
		fmt.Println("key", k)
		fmt.Println("val:", strings.Join(v, ""))
	}
	fmt.Fprintf(w, "hello david")
}

func main() {
	//http.Handle("/", Hello{})
	http.Handle("/string", String("I'm a frayed knot."))
	http.Handle("/struct", &Struct{"Hello", ":", "Gophers!"})
	//err := http.ListenAndServe("localhost:4000", nil)

	http.HandleFunc("/hello", sayhelloName)
	//var h Hello
	err := http.ListenAndServe("localhost:9090", nil)

	if err != nil {
		log.Fatal("ListenAndServe: ", err.Error())
	}
}
