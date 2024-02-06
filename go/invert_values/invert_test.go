package invertvalues

import (
	"reflect"
	"testing"
)

func TestInvert(t *testing.T) {
	tests := []struct {
		name string
		arr  []int
		want []int
	}{
		{"Basic Functionality", []int{1, -2, 3, -4, 0}, []int{-1, 2, -3, 4, 0}},
		{"All Positive Values", []int{1, 2, 3}, []int{-1, -2, -3}},
		{"All Negative Values", []int{-1, -2, -3}, []int{1, 2, 3}},
		{"Single Element", []int{5}, []int{-5}},
		{"Large Numbers", []int{1000000, -1000000}, []int{-1000000, 1000000}},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := Invert(tt.arr); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("Invert() = %v, want %v", got, tt.want)
			}
		})
	}
}
