class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:

        meetings.sort()
        available_rooms = list(range(n))
        heapq.heapify(available_rooms)

        ongoing_meetings = []

        room_meeting_count = [0] * n

        for start, end in meetings:
            
            while ongoing_meetings and ongoing_meetings[0][0] <= start:
                end_time, room = heapq.heappop(ongoing_meetings)
                heapq.heappush(available_rooms, room)

            if available_rooms:
                room = heapq.heappop(available_rooms)
                heapq.heappush(ongoing_meetings, (end, room))
            else:
                earliest_end, room = heapq.heappop(ongoing_meetings)
                delay = end - start
                new_end = earliest_end + delay
                heapq.heappush(ongoing_meetings, (new_end, room))
            
            room_meeting_count[room] += 1
        
        max_meetings = max(room_meeting_count)
        for i in range(n):
            if room_meeting_count[i] == max_meetings:
                return i
        