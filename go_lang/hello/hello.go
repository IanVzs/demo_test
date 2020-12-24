package main

import (
        "fmt"
        "log"
        "example.com/greetings"
)

func dosome(name string) {
        message, err := greetings.Hello(name)
        if err != nil {
                log.Fatal(err)
        }

        fmt.Println(message + "\n")
}

func main() {
        // Get a greeting message and print it.
        // Set properties of the predefined Logger, including
        // the log entry prefix and a flag to disable printing
        // the time, source file, and line number.
        fmt.Println("传入值:")
        dosome("Ian You")
        fmt.Println("传入空:")
        dosome("")
}
