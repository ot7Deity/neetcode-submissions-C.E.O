class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas)<sum(cost):
            return -1
        # how much gas we have and do we have enough for the cost
        total=0
        #the index of our answer 
        res=0
        #can do this because they are same len
        for i in range(len(gas)):
            #gives you how much gas you will have after collecting gas the subtracting cost
            total+=gas[i]-cost[i]

            if total<0:
                total=0
                res= i +1
        return res

        