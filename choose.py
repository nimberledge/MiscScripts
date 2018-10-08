def choose_k(elements, k):
	if not elements or k == 0:
		return []

	solutions = []
	for index, element in enumerate(elements):
		temp_set = list(elements)
		temp_set = temp_set[index+1:]
		if len(temp_set) < k-1:
			break
		picks = choose_k(temp_set, k-1)
		
		if picks == []:
			solutions.append([element])

		for pick in picks:
			solution = list(pick)
			solution.append(element)
			solutions.append(solution)
	
	return solutions

if __name__ == "__main__":
	test = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
	all_ways = choose_k(test, 5)
	for way in all_ways:
		print way
	print len(all_ways)
