#brute force
class Solution(object):
    def Intersection(self, arr1, arr2):
        intersection=[]
        visited=[0]*len(arr2)
        for i in range(len(arr1)):
            for j in range(len(arr2)):
                if arr1[i]==arr2[j] and visited[j]==0:
                    intersection.append(arr1[i])
                    visited[j]=1
                    break
        return intersection
obj=Solution()
arr1=[1,1,1,2,2,3]
arr2=[1,2,2,2,3,3]
print(obj.Intersection(arr1,arr2))

#optimal solution

class Solution(object):
    def Intersection(self, arr1, arr2):
        intersection=[]
        i=0
        j=0
        while i<len(arr1) and j<len(arr2):
            if arr1[i]<arr2[j]:
                i+=1
            elif arr2[j]<arr1[i]:
                j+=1
            else:
                intersection.append(arr1[i])
                i+=1
                j+=1
                
            
        
        return intersection
obj=Solution()
arr1=[1,1,1,2,2,3]
arr2=[1,2,2,2,3,3]
print(obj.Intersection(arr1,arr2))




#Interview tip

#This is the expected optimal solution for Intersection of Two Sorted Arrays when duplicates are allowed.

#If the interviewer asks for unique intersection only, then change the else block to:

#else:
 #   if len(intersection) == 0 or intersection[-1] != arr1[i]:
  #      intersection.append(arr1[i])
   # i += 1
    #j += 1
                