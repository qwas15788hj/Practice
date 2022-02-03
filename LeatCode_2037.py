class Solution(object):
    def minMovesToSeat(self, seats, students):
        count = 0
        for i in range(len(seats)):
            count += abs(max(seats)-max(students))
            seats.remove(max(seats))
            students.remove(max(students))
            
        return count