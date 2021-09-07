# FCFS

# Function to find the waiting
# time for all processes
def findWaitingTime(processes, n,
					bt, wt):

	# waiting time for
	# first process is 0
	wt[0] = 0

	# calculating waiting time
	for i in range(1, n ):
		wt[i] = bt[i - 1] + wt[i - 1]

# Function to calculate turn
# around time
def findTurnAroundTime(processes, n,
					bt, wt, tat):

	# calculating turnaround
	# time by adding bt[i] + wt[i]
	for i in range(n):
		tat[i] = bt[i] + wt[i]

# Function to calculate
# average time
def findavgTime( processes, n, bt):

	wt = [0] * n
	tat = [0] * n
	total_wt = 0
	total_tat = 0

	# Function to find waiting
	# time of all processes
	findWaitingTime(processes, n, bt, wt)

	# Function to find turn around
	# time for all processes
	findTurnAroundTime(processes, n,
					bt, wt, tat)

	# Display processes along
	# with all details
	print( "Process# Burst_time " +
				" Waiting_time " +
				" Turn_around_time")

	# Calculate total waiting time
	# and total turn around time
	for i in range(n):
	
		total_wt = total_wt + wt[i]
		total_tat = total_tat + tat[i]
		print(" " + str(i + 1) + "\t\t" +
					str(bt[i]) + "\t " +
					str(wt[i]) + "\t\t " +
					str(tat[i]))

	print( "Average waiting time = "+
				str(total_wt / n))
	print("Average turn around time = "+
					str(total_tat / n))

# Driver code
if __name__ =="__main__":
	
	# creating an empty list
	processes = []
	
	# number of elements as input
	p = int(input("\nEnter the no of processes: "))
	
	# iterating till the range
	for i in range(0, p):
		
	# Taking input from the user

		ele = i
	
		processes.append(ele)

	# creating an empty list
	burst_time = []
	# number of elements as input

	
	# iterating till the range
	for i in range(0, p):

		ele = int(input(f'Enter burst_time of #{i+1} process : '))
	
		burst_time.append(ele)
		# Example: burst_time = [10, 5, 8]

	findavgTime(processes, p, burst_time)
