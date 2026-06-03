class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        left = 0
        right = len(people)-1
        people.sort()
        output = 0
        while left <= right:
            remain = limit - people[right]
            right-=1
            output+=1
            if left<=right and remain >= people[left]:
                left+=1
        return output


        