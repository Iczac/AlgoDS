def merge(left, right):
	array = []
	inv_count = 0

	while len(left) > 0 or len(right) > 0:
		if len(left) > 0 and len(right) > 0:
			if left[0] < right[0]:
				array.append(left[0])
				left = left[1:]
			else:
				array.append(right[0])
				right = right[1:]
				inv_count += len(left)

		elif len(left) > 0:
			array.append(left[0])
			left = left[1:]

		else:
			array.append(right[0])
			right = right[1:]

	return array, inv_count


def sort(array):
	array_len = len(array)
	if array_len <= 1:
		return array, 0

	left, x = sort(array[:(array_len/2)])
	right, y = sort(array[(array_len/2):])
	array, z = merge(left, right)

	return array, x+z+y
