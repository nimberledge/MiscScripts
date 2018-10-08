import time
part_table = {}

def partitions(n, backoff = None):
	if n == 0:
		part_table[n] = [[]]

	if n == 1:
		part_table[n] = [[1]]

	if n in part_table:
		return part_table[n]

	parts = []
	start = 1
	if backoff:
		start = backoff
	for i in range(start, n//2+1):
		j = n - i
		p1 = partitions(i, backoff = i)
		p2 = partitions(j, backoff = i)
		for first in p1:
			for second in p2:
				part = first + second
				part.sort()
				if part not in parts:
					parts.append(part)
	parts.append([n])
	part_table[n] = parts
	return parts

if __name__ == "__main__":
	n = int(input("Enter number to partition:"))
	start = time.time()
	those = partitions(n)
	taken = time.time() - start
	count = 0
	for one in those:
		flag = 0
		for each in one:
			if each > 6:
				flag = 1
				break
		if (flag == 1 or len(one) != 3):
			continue
		print ('+'.join([str(it) for it in one]))
		count += 1
	print (len(those), 'partitions totally')
	print (count, 'ways on a dice')
	print (taken)
