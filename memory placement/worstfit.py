# Worst - Fit algorithm

def worstFit(blockSize, m, processSize, n):
	
	# Stores block id of the block
	# allocated to a process
	
	# Initially no block is assigned
	# to any process
	allocation = [-1] * n
	
	# pick each process and find suitable blocks
	# according to its size and assign to it
	for i in range(n):
		
		# Find the best fit block for
		# current process
		wstIdx = -1
		for j in range(m):
			if blockSize[j] >= processSize[i]:
				if wstIdx == -1:
					wstIdx = j
				elif blockSize[wstIdx] < blockSize[j]:
					wstIdx = j

		# If we could find a block for
		# current process
		if wstIdx != -1:
			
			# allocate block j to p[i] process
			allocation[i] = wstIdx

			# Reduce available memory in this block.
			blockSize[wstIdx] -= processSize[i]

	print("\nProcess No. Process Size Block no.")
	for i in range(n):
		print(i + 1, "		 ",
			processSize[i], end = "	 ")
		if allocation[i] != -1:
			print(allocation[i] + 1)
		else:
			print("Not Allocated")

# Driver code
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

	worstFit(blockSize, m, processSize, n)

