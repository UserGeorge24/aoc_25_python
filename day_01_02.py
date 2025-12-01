from math import floor
from day_01_01 import day_01

class day_01_02(day_01):
    
    def truncate_number(self, row):
        
        if len(row) > 3:
            self.sum_of_zeros += int( row[1] )
            self.number = int( row[1:] ) % 100  
        else:
            self.number = int( row[1:] )

    def calc_next_value(self):
        
        if self.direction == '+':
            self.next_value += self.number

            self.sum_of_zeros += 1 if self.next_value > 100 else 0

            self.next_value = self.next_value % 100 if self.next_value >= 100 else self.next_value
        else:
            if self.number > self.next_value:
                self.sum_of_zeros += 1 if self.next_value != 0 else 0
                self.next_value = ( self.next_value + 100 ) - self.number
            else:
                self.next_value -= self.number

        self.sum_of_zeros = self.sum_of_zeros + 1 if self.next_value == 0 else self.sum_of_zeros

def main(file_path: str = "src_01") -> None:
    
    obj = day_01_02()
    obj.set_starting_value()

    with open(file_path, 'r') as file:
        for row in file:
            obj.set_direction(row)
            obj.truncate_number(row.replace('\n',''))
            obj.calc_next_value()

    print(obj.get_sum_of_zeroes())


if __name__ == "__main__":
    main()


