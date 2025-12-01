

class day_01:
    
    direction = ''
    number = 0
    next_value = 0
    sum_of_zeros = 0
    
    def set_direction(self, row):
        
        self.direction = '+' if row[:1] == 'R' else '-'
        
    def truncate_number(self, row):
        
        self.number = int( row[1:] ) if len(row) <= 3 else int( row[1:] ) % 100
  
    def set_starting_value(self):
        
        self.next_value = 50

    def calc_next_value(self):
        
        if self.direction == '+':
            self.next_value += self.number
            self.next_value = self.next_value % 100 if self.next_value >= 100 else self.next_value
        else:
            if self.number > self.next_value:
                self.next_value = ( self.next_value + 100 ) - self.number
            else:
                self.next_value -= self.number

        self.sum_of_zeros = self.sum_of_zeros + 1 if self.next_value == 0 else self.sum_of_zeros

    def get_sum_of_zeroes(self):
        
        return self.sum_of_zeros

if __name__ == "__main__":

    file_path = "src_01"

    object = day_01()

    object.set_starting_value()

    with open(file_path, 'r') as file:
        for row in file:
            object.set_direction(row)
            object.truncate_number(row)
            object.calc_next_value()

    print(object.get_sum_of_zeroes())