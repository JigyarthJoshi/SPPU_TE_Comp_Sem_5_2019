import threading  
import time

# Shared Memory variables
CAPACITY = 10  #size of the buffer
buffer = [-1 for i in range(CAPACITY)]  #initially buffer is empty
in_index = 0    #index where the producer enters item
out_index = 0   ##index where the consumers takes the item
#both initially zero

# Declaring Semaphores
mutex = threading.Semaphore()  # This semaphore variable is used to achieve mutual exclusion between processes. By using this variable, either Producer or Consumer will be allowed to use or access the shared buffer at a particular time. This variable is set to 1 initially.
empty = threading.Semaphore(CAPACITY)  #This semaphore variable is used to define the empty space in the buffer. Initially, it is set to the whole space of the buffer i.e. "n" because the buffer is initially empty.
full = threading.Semaphore(0)  #This semaphore variable is used to define the space that is filled by the producer. Initially, it is set to "0" because there is no space filled by the producer initially.
 
# Producer Thread Class
class Producer(threading.Thread):
  def run(self):
     
    global CAPACITY, buffer, in_index, out_index
    global mutex, empty, full
     
    items_produced = 0
    counter = 0
     
    while items_produced < 20:  #producer will produce 20 items
      empty.acquire()   #wait 
      mutex.acquire()  #critical section will be with the producer
       
      counter += 1
      buffer[in_index] = counter      #place item in buffer
      in_index = (in_index + 1) % CAPACITY      
      print("Producer produced : ", counter)
       
      mutex.release()     #signal mutex 
      full.release()
       
      time.sleep(1.5)
       
      items_produced += 1
 
# Consumer Thread Class
class Consumer(threading.Thread):
  def run(self):    #
     
    global CAPACITY, buffer, in_index, out_index, counter
    global mutex, empty, full
     
    items_consumed = 0
     
    while items_consumed < 20:
      full.acquire()        #wait (apply mutex lock)
      mutex.acquire()
       
      item = buffer[out_index]
      out_index = (out_index + 1) % CAPACITY
      print("Consumer consumed item : ", item)
       
      mutex.release()   #signal  (release mutex lock)
      empty.release()      
       
      time.sleep(2)
       
      items_consumed += 1
 
# Creating Threads
producer = Producer()
consumer = Consumer()
 
# Starting Threads
consumer.start()
producer.start()
 
# Waiting for threads to complete
producer.join()
consumer.join()