// Day - 12
// Problem - 20
// Valid Parantheses

// Still Checking our Go.

func isValid(s string) bool {
    stack := []rune{}
    pairs := map[rune]rune{')': '(', '}': '{', ']': '['}

    for _, char := range s {
        if char == '(' || char == '{' || char == '[' {
            stack = append(stack, char) // Push opening brackets
        } else {
            if len(stack) == 0 || stack[len(stack)-1] != pairs[char] {
                return false // Mismatch or empty stack
            }
            stack = stack[:len(stack)-1] // Pop matching bracket
        }
    }

    return len(stack) == 0
}
