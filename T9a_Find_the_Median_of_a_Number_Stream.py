# https://github.com/cl2333/Grokking-the-Coding-Interview-Patterns-for-Coding-Questions/blob/master/9.%20Pattern%20Two%20Heaps/Find%20the%20Median%20of%20a%20Number%20Stream%20(medium).py
# _Topic_ @9 Pattern: Pattern Two Heaps
# _Q_ @9. a)
# _Difficulty_ medium
# Time taken until for own solution, without compiling the code: 30 min

# Problem Statement
"""
Design a class to calculate the median of a number stream. The class should have the following two methods:
insertNum(int num): stores the number in the class
findMedian(): returns the median of all numbers inserted in the class
If the count of numbers inserted in the class is even, the median will be the average of the middle two numbers.
Example 1:
1. insertNum(3)
2. insertNum(1)
3. findMedian() -> output: 2
4. insertNum(5)
5. findMedian() -> output: 3
6. insertNum(4)
7. findMedian() -> output: 3.5
"""

# My solution
from heapq import *

class MY_MedianOfAStream:
	# My solution (2 below)
	minHeap = []
	maxHeap = []
	
	def insert_num(self, num):
		# check to which heap it should go
		# check sizes of heaps to see if things need to be 
		# moved from one heap to another...

		if len(self.minHeap) == len(self.maxHeap) + 1:
			# next maxHeap needs extra thing.
			# it doesn't need evening out
			if num <= self.minHeap[0]: # access smallest element without popping.
				heappush(self.maxHeap, num)
			# it does
			else:
				heappush(self.maxHeap, heappop(self.minHeap))
				heappush(self.minHeap, num)
		elif len(self.minHeap) == len(self.maxHeap) and len(self.minHeap) != 0:
			# now it has to go to minHeap.
			if num >= self.minHeap[0]: # access smallest element without popping.
				heappush(self.minHeap, num)
			# it does
			else:
				heappush(self.minHeap, heappop(self.maxHeap))
				heappush(self.maxHeap, num)
		else:
			heappush(self.minHeap, num)
			print("start??")

	def find_median(self):
		# if uneven lengths:
		if len(self.minHeap) == len(self.maxHeap) + 1:
			return self.minHeap[0]
		# if even take average (ignore integer overflow for now...)
		elif len(self.minHeap) == len(self.maxHeap):
			# self.maxHeap[-1] is O(log(n)) and so defeats the purpose.
			# now I get why there were negative signs for the max_hep all along.
			# why isn't there just the option for  maxheap. At least I kind of get it now.
			return (self.minHeap[0]+self.maxHeap[-1]) / 2
		else:
			print("Error? Seems invalid heap length")


## ANSWER
## Python only has min-heap, so need negative signs when building "max-heap"
class MedianOfAStream:
	maxHeap = []  # containing first half of numbers
	minHeap = []  # containing second half of numbers

	def insert_num(self, num):
		# 1) add to correct heap with inversion (-ve) if necessary
		# 2) then restructure the heaps if necessary
		# why did putting the "not self.maxHeap" in front work all of a sudden...?
		if not self.maxHeap or -self.maxHeap[0] >= num:  # 1)
			heappush(self.maxHeap, -num)
		else:
			heappush(self.minHeap, num)

		# either both the heaps will have equal number of elements or max-heap will have one
		# more element than the min-heap, if not below
		if len(self.maxHeap) > len(self.minHeap) + 1:  # 2)
			heappush(self.minHeap, -heappop(self.maxHeap))
		elif len(self.maxHeap) < len(self.minHeap):
			heappush(self.maxHeap, -heappop(self.minHeap))

	def find_median(self):
		if len(self.maxHeap) == len(self.minHeap):
			# we have even number of elements, take the average of middle two elements
			return -self.maxHeap[0] / 2.0 + self.minHeap[0] / 2.0

		# because max-heap will have one more element than the min-heap
		return -self.maxHeap[0] / 1.0  # to have decimals...?

""" Asymptotics:
For sols: insert_num() = inserting a number into the heap means, the heap has to be 
	heapified(?) again and so O(log (n)) time.
	find_median() = O(1) <- because just pick up top number(s) from heap.
For mine: find_median should be the same and insert_num should also be the same, 
	same heap-specific methods are being  used (heappush & heappop)
Space complexity: O(n) <- however many numbers you add to the heap
"""


# Additional code
def main():
	print("My answer:")
	medianOfAStream = MY_MedianOfAStream()
	medianOfAStream.insert_num(3)
	medianOfAStream.insert_num(1)
	print("The median is: " + str(medianOfAStream.find_median()))
	medianOfAStream.insert_num(5)
	print("The median is: " + str(medianOfAStream.find_median()))
	medianOfAStream.insert_num(4)
	print("The median is: " + str(medianOfAStream.find_median()))

	print("Solutions:")
	medianOfAStream = MedianOfAStream()
	medianOfAStream.insert_num(3)
	medianOfAStream.insert_num(1)
	print("The median is: " + str(medianOfAStream.find_median()))
	medianOfAStream.insert_num(5)
	print("The median is: " + str(medianOfAStream.find_median()))
	medianOfAStream.insert_num(4)
	print("The median is: " + str(medianOfAStream.find_median()))

main()
