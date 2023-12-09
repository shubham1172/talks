# Snippets

This contains snippets from my talk.

## Errors in Go

```go
type error interface {
    Error() string
}
```

```go
// src: strconv stdlib
// convert string to int
func Atoi(s string) (int, error)

n, err := strconv.Atoi("42")
if err != nil {
    log.Fatal(err)
}
// Do something with n
```

## Returning errors

TODO