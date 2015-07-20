package main

import (
	"bytes"
	"fmt"
	"io"
	"io/ioutil"
	"mime/multipart"
	"net/http"
	"os"
)

func postFile(filename string, targetUrl string) error {
	bodyBuf := &bytes.Buffer{}
	bodyWriter := multipart.NewWriter(bodyBuf)
	contentType := bodyWriter.FormDataContentType()
	fileWriter, err := bodyWriter.CreateFormFile("uploadfile", filename)
	if err != nil {
		fmt.Println("error writing to buffer")
		return err
	}
	file, err := os.Open(filename)
	if err != nil {
		fmt.Println("error opening file")
		return err
	}
	defer file.Close()
	_, err = io.Copy(fileWriter, file)
	if err != nil {
		return err
	}
	bodyWriter.Close()

	resp, err := http.Post(targetUrl, contentType, bodyBuf)
	if err != nil {
		return err
	}
	defer resp.Body.Close()
	resp_body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		return err
	}
	fmt.Println(resp.Status)
	fmt.Println(string(resp_body))
	return nil
}

func main() {
	targetUrl := "http://localhost:9090/upload"
	filename := "./hello.txt"
	postFile(filename, targetUrl)
}
