package {{ cookiecutter.package_name }}

import "fmt"

// Hello is a dummy public function. Replace with the real API.
func Hello(name string) string {
	if name == "" {
		name = "world"
	}
	return fmt.Sprintf("hello, %s", name)
}
