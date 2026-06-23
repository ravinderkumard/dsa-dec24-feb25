1class Solution:
2    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
3        total_gas = sum(gas)
4        total_cost = sum(cost)
5        
6        if total_gas<total_cost:
7            return -1
8        current_gas = 0
9        start = 0
10        for i in range(len(gas)):
11            current_gas += gas[i] - cost[i]
12            if current_gas<0:
13                start = i+1
14                current_gas = 0
15
16
17        return start