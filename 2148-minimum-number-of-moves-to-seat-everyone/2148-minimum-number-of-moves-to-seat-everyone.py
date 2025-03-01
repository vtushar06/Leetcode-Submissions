class Solution(object):
    def minMovesToSeat(self, seats, students):
        moves=0
        seats.sort()
        students.sort()
        i=0
        while(i<len(seats)):
            moves+=abs(seats[i]-students[i])
            i+=1
        return moves    
