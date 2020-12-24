package greetings

import (
        "fmt"
        "errors"
)

// Hello returns a greeting for the named person.
func Hello(name string) (string, error) {
        // Return a greeting that embeds the name in a message.
        // If no name, ret an error.
        if name == "" {
                return "", errors.New("empty name")
        }
        message := fmt.Sprintf("Hi, %v. Welcome!", name)
        return message, nil
}
