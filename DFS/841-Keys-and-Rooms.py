class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        no_of_rooms = len(rooms)

        self.count = 1
        visited_key = [0]
        def dfs(idx):
              
            key_list = rooms[idx]

            for each_key in key_list:
                if each_key in visited_key:
                    continue
                visited_key.append(each_key)  
                self.count+=1
                dfs(each_key)
        
        dfs(0)
        print(self.count)
        return self.count==no_of_rooms