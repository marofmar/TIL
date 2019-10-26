// 1. ASCII art title <A dog>

package main

import "fmt" 

func main() {
  fmt.Println("  __      _")
  fmt.Println("o'')}____//")
  fmt.Println(" `_/      )")
  fmt.Println(" (_(_/-(_/")
}

// 2. variable which is actively using memory so that if not assigining value in it, Go raises error.

package main 
import "fmt" 
func main() {
  var jellybeanCounter int8
  jellybeanCounter = 17
  fmt.Println(jellybeanCounter) 
}
