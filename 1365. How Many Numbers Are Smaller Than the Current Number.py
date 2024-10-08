# QUESTION
# Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

# Return the answer in an array.

 

# Example 1:

# Input: nums = [8,1,2,2,3]
# Output: [4,0,1,1,3]
# Explanation: 
# For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3). 
# For nums[1]=1 does not exist any smaller number than it.
# For nums[2]=2 there exist one smaller number than it (1). 
# For nums[3]=2 there exist one smaller number than it (1). 
# For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).
# Example 2:

# Input: nums = [6,5,4,8]
# Output: [2,1,0,3]
# Example 3:

# Input: nums = [7,7,7,7]
# Output: [0,0,0,0]

## Approach: define a new list containing the sorted elements of nums so that for any element in new_list the number of elements smaller than it will be the index position
#example if the list contains [8,6,9,2] the sortd list contains[2,6,8,9] the number of elements smaller than 2 is 0 and 6 is 1 which all are their corresponding index values
#so using elements as key and index as value add it to a dictionary
# again using a loop ,this time using original array nums iterate through the elements and retreive their vaue from dictionary . you cand add it to a new list and return 
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        new_list=sorted(nums)#the sorted elements are added to new_list
        
        
        output_list=[]
        output={}
        for i in range(0,len(new_list)):
            if new_list[i] not in output:
                output[new_list[i]]=i
         
                    
        for i in range(len(nums)):
            output_list.append(output[nums[i]])
        return output_list    
