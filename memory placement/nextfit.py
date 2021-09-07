# Next fit memory management algorithm

def NextFit(blockSize, m, processSize, n):
	
	# Stores block id of the block allocated to a process

	# Initially no block is assigned to any process
	allocation = [-1] * n
	j = 0

	# pick each process and find suitable blocks according to its size and assign to it
	for i in range(n):

		# Do not start from beginning
		while j < m:

			if blockSize[j] >= processSize[i]:

				# allocate block j to p[i] process
				allocation[i] = j

				# Reduce available memory in this block.
				blockSize[j] -= processSize[i]

				break

			# mod m will help in traversing the blocks from starting block after we reach the end.
			j = (j + 1) % m

	print("\nProcess No. Process Size Block no.")
	for i in range(n):
		print(i + 1, "		 ", processSize[i],
									end = "	 ")
		if allocation[i] != -1:
			print(allocation[i] + 1)
		else:
			print("Not Allocated")

# Driver Code
if __name__ == '__main__':

	# creating an empty list
	blockSize = []
	
	# number of elements as input
	p = int(input("\nEnter the no of blocks: "))
	
	# iterating till the range
	for i in range(0, p):
		
	# Taking input from the user

		ele = int(input(f'Enter block size of #{i+1} block : '))
	
		blockSize.append(ele)

	# creating an empty list
	processSize = []
	# number of elements as input
	q = int(input("\nEnter the no of processes : "))
	
	# iterating till the range
	for i in range(0, q):

		ele = int(input(f'Enter process size of #{i+1} process : '))
	
		processSize.append(ele)


	m = len(blockSize)
	n = len(processSize)

	NextFit(blockSize, m, processSize, n)
	
