
class day_02:

    def __init__(self):
        self.ranges = []
        self.invalid_ids = []
    
    def separate_ranges(self, row):

        temp_list = []

        splitted_row = row.split(',')

        for value in splitted_row:
            if value != '':
                one_range = str( value ).split('-')

                temp_list.clear()
                temp_list.insert(0, int( one_range[1] ))
                temp_list.insert(0, int( one_range[0] ))

                index = len(self.ranges) + 1 if len(self.ranges) > 0 else 0

                self.ranges.insert(index,temp_list[:])
    
    def find_invalid_ids(self, ranges):

       for i in range(ranges[0],ranges[1] + 1):
#       work with unmatched numbers only          
            i = str(i)
            if len(i) % 2 == 0:
                first_half = i[:len(i)//2]
                second_half = i[len(i)//2:]

                if first_half == second_half:
                    self.invalid_ids.append(i)

def main() -> None:
    
    path = 'src_02'

    object = day_02()

    with open(path, 'r') as file:
        for row in file:
            object.separate_ranges(row.replace('\n',''))

    for range in object.ranges:
        object.find_invalid_ids(range)
    
    print(f'Sum of Invalid IDs: {sum(int(i) for i in object.invalid_ids)}')

if __name__ == "__main__":
    main()
