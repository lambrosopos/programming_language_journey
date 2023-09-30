package main

import (
	"fmt"
	"os"
	"path/filepath"
)

func main() {
	if len(os.Args) < 3 {
		fmt.Println("Need 2 or more arguments. Ex) main.go word filepath")
		return
	}

	word := os.Args[1]
	files := os.Args[2:]

	fmt.Println("Looking for word:", word)
	PrintAllFiles(files)
}

func GetFileList(path string) ([]string, error) {
	return filepath.Glob(path)
}

func PrintAllFiles(files []string) {
	for _, path := range files {
		filelist, err := GetFileList(path)
		if err != nil {
			fmt.Println("Wrong filepath. err:", err, "path:", path)
			return
		}

		fmt.Println("File list to look for")
		for _, name := range filelist {
			fmt.Println(name)
		}
	}
}
