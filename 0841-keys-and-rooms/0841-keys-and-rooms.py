class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        rooms_left = [i for i in range(len(rooms))]
        # print(f'rooms_left: {rooms_left}')

        def traverse(room_index, room_keys):
            # print(f'Visiting Room {room_index}')
            rooms_left.remove(room_index)
            for i in room_keys:
                if i in rooms_left:
                    traverse(i, rooms[i])

        traverse(0, rooms[0])

        if rooms_left:
            return False
        else:
            return True