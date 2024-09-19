

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
