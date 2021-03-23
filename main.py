# Author: Daniel Salazar
import sys
import os

class MovieTheater:

    def __init__(self, rows, cols):
        self.rows = rows//2
        self.cols = cols
        # Seat matrix to track which seats are reserved
        self.seats = [[True]*cols for i in range(rows//2)]
        #dividing number of rows by two since every alternate row is blocked

    # Convert letter to number in matrix
    def __get_seat_number(self,i,j):
        return 'ACEGI'[i] + str(j+1)

    # Find and return next empty seat, and return -1, -1 if none available
    def __next_empty_seat(self,seat):
        for x in range(seat[0],self.rows):
            for y in range(seat[1],self.cols):
                if self.seats[x][y]:
                    return (x,y)
        return (-1,-1)

    # Returns seats in next row
    def __next_seat(self,seat):
        if seat[1]+1 >= self.cols:
            return (seat[0]+1,0)
        return (seat[0],seat[1]+1)

    # Boundries
    def __check_seat_in_bounds(self,seat):
        return seat[0]<self.rows and seat[1]<self.cols
    
    # Only public method in class, checks for enough seats available to seat group. Once we find the seats, we fill the seats and 3 buffer seats
    def assign_seat(self, number_of_seats):
        next_empty_seat = self.__next_empty_seat((0,0))
        assigned = []
        # Find first empty seat and check if there are enough colums for the entire group
        while(self.cols-next_empty_seat[1]<number_of_seats and next_empty_seat!=(-1,-1)):
            next_empty_seat = self.__next_empty_seat(self.__next_seat(next_empty_seat))
        if(next_empty_seat == (-1,-1)):
            return []
        # Assign seats to the group
        while(self.__check_seat_in_bounds(next_empty_seat) and len(assigned)<number_of_seats):
            assigned.append(next_empty_seat)
            self.seats[next_empty_seat[0]][next_empty_seat[1]] = False
            next_empty_seat = self.__next_seat(next_empty_seat)
        buffer = 3
        current_row = next_empty_seat[0]
        current_col = next_empty_seat[1]
        # Add 3 seat buffer
        while current_col<self.cols and buffer>0:
            self.seats[current_row][current_col] = False
            current_col+=1
            buffer-=1
        # Returns seat in format readable to matrix
        return list(map(lambda x: self.__get_seat_number(x[0],x[1]),assigned))
    

def main(input_file_name):
    movieTheater = MovieTheater(10,20)
    reservation_requests = []
    # Parse input file
    with open(input_file_name,'r') as f:
        reservation_requests = f.read().split('\n')
    # Start writing output to file
    with open('reservations.txt','w') as output:
        # Iterate through each reservation request
        for reservation_request in reservation_requests:
            if reservation_request: 
                # Take each individual request and split it to read it
                reservation_id,number_of_seats = reservation_request.split(' ')
                assigned_seats = movieTheater.assign_seat(int(number_of_seats))
                # Write numbers with commas separating
                output.write(reservation_id + " "+ ','.join(assigned_seats) + "\n")
    # Print file path to console
    output_file_path = os.path.abspath(output.name)
    print("Output file : ", os.path.abspath(output.name))
    return output_file_path

if __name__ == "__main__":
    input_file_name = sys.argv[1]
    main(input_file_name)