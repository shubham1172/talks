package snippets

import (
	"log"
	"strconv"
)

type error interface {
	Error() string
}

// src: strconv stdlib
// convert string to int
func Atoi(s string) (int, error) {
	// implementation
	return 0, nil
}

func main() {
	n, err := strconv.Atoi("42")
	if err != nil {
		log.Fatal(err)
	}
	// Do something with n
	log.Println(n)
}
