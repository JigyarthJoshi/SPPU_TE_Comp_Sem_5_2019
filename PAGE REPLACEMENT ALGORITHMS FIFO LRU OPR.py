# Python3 implementation of FIFO page replacement in Operating Systems.

# Function to find page faults using FIFO 
def FIFO(pages, capacity):
    from queue import Queue       
    # To represent set of current pages. We use an unordered_set so that we quickly check if a page is present in set or not 
    s = set() 
  
    # To store the pages in FIFO manner 
    indexes = Queue() 
  
    # Start from initial page 
    page_faults = 0
    for i in range(len(pages)):
          
        # Check if the set can hold more pages 
        if (len(s) < capacity):
              
            # Insert it into set if not present already which represents page fault 
            if (pages[i] not in s):
                s.add(pages[i]) 
                # increment page fault 
                page_faults += 1 
                # Push the current page into the queue 
                indexes.put(pages[i]) 
        # If the set is full then need to perform FIFO i.e. remove the first page of the queue from set and queue both and insert the current page 
        else:
              
            # Check if current page is not already present in the set 
            if (pages[i] not in s):
                  
                # Pop the first page from the queue 
                val = indexes.queue[0] 
  
                indexes.get() 
  
                # Remove the indexes page 
                s.remove(val) 
  
                # insert the current page 
                s.add(pages[i]) 
  
                # push the current page into  the queue 
                indexes.put(pages[i]) 
  
                # Increment page faults 
                page_faults += 1
  
    return page_faults


# Python3 program for page replacement algorithm

def lru(pages, capacity):                   
    # List of current pages in Main Memory
    s = []

    pageFaults = 0
    # pageHits = 0

    for i in pages:

        # If i is not present in currentPages list
        if i not in s:

            # Check if the list can hold equal pages
            if(len(s) == capacity):
                s.remove(s[0])
                s.append(i)

            else:
                s.append(i)

            # Increment Page faults
            pageFaults +=1

        # If page is already there in currentPages i.e in Main
        else:    
            # Remove previous index of current page
            s.remove(i)
            # Now append it, at last index
            s.append(i)
	
    return pageFaults

def opt(pages, capacity):
    fault = 0
    frameList = [-1] * capacity     # all are zero intially
    point = 0

    for i in range(len(pages)):

        if point < capacity:  #if frame has less pages than capacity insert pages one by one till size of frame reaches max capacity

            frameList[i] = pages[i]
            fault += 1      #increment page fault
            point += 1      #increment index

        elif frameList.count(pages[i]) == 0:

            fault += 1
            checkFar = [1] * capacity  

            for j in range(i+1, len(pages)): #check farthest in the list

                if checkFar.count(1) <= 1:     #if current page is present in frame do nothing
                    break

                if frameList.count(pages[j]) != 0:   
                    checkFar[frameList.index(pages[j])] = 0
                    
            frameList[checkFar.index(1)] = pages[i]  #replace the page 

    return fault

if __name__ == '__main__':
    print("Enter the space seperated reference string:", end = "")
    pages = list(map(int, input().split())) #Page Reference String
    n = len(pages) 
    capacity = int(input("Enter Frame Size: ")) #Frame Size
    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("For FIFO page replacement Enter 1 ")
    print ("For LRU page replacement Enter 2 ")
    print ("For Optimal page replacement Enter 3 ")
    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    choice = int(input())

    if choice == 1:
            print ("~~~~~~~~~FIFO~~~~~~~~~")
            print ("Entered reference string is: ", pages, "\nEntered frame size is: ", capacity)
            print("The number of faults is: ", end = "")
            p = FIFO(pages, capacity)
            print (p)
            print(f'The fault ratio is: {p}/{len(pages)}')
    elif choice == 2:
            print ("~~~~~~~~~LRU~~~~~~~~~")
            print ("Entered reference string is: ", pages, "\nEntered frame size is: ", capacity)
            print("The number of faults is: ", end = "")
            p = lru(pages, capacity)
            print (p)
            print(f'The fault ratio is: {p}/{len(pages)}')
    elif choice == 3:
            print ("~~~~~~~~~OPR~~~~~~~~~")
            print ("Entered reference string is: ", pages, "\nEntered frame size is: ", capacity)
            print("The number of faults is: ", end = "")
            p = opt(pages, capacity)
            print (p)
            print(f'The fault ratio is: {p}/{len(pages)}')
    else:
            print("Invalid Input")    