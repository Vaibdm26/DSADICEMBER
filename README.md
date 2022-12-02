# DSADICEMBER
# Function to calculate the sum
# of all odd length subarrays

def OddLengthSum(arr):
	# Stores the sum
	sum = 0

	# Size of array
	l = len(arr)

	# Traverse the array
	for i in range(l):

		# Generate all subarray of
		# odd length
		for j in range(i, l, 2):
			for k in range(i, j + 1, 1):

				# Add the element to sum
				sum += arr[k]
			
	# Return the final sum
	return sum

# Driver Code

# Given array arr[]
arr = [ 1, 5, 3, 1, 2 ]

# Function call
print(OddLengthSum(arr))
