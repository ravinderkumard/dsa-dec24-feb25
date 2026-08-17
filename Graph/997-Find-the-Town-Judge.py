class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        """
            Idea is to build the adj list
            and try to populate the people who trust other
            and if any element don't trust will have empty list.
            that will be the judge.
        """
        people_list = [0]*(n+1)

        for a,b in trust:
            people_list[a]-=1
            people_list[b]+=1


        for person in range(1,n+1):
            if people_list[person]==n-1:
                return person

        return -1