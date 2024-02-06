package invertvalues

// Invert Given a set of numbers, return the additive inverse of each. Each positive becomes negatives, and the negatives become positives.
func Invert(arr []int) []int {
	var arrNew []int
	for _, value := range arr {
		arrNew = append(arrNew, value*-1)
	}
	return arrNew
}
