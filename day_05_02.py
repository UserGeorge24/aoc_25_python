
class day_05:
    
    def __init__(self):
        
        self.fresh_id_ranges = []
        self.new_range = []
    
    def get_number_of_ranges(self):
        count = 0
        for i in self.fresh_id_ranges:
            count += (i[len(i)-1] + 1) - i[0]
            
        return count
    
    def create_ranges(self):
        
        found = False
        
        for j in self.fresh_id_ranges:
            
            moved = False
            
            for index, i in enumerate(self.new_range):
            
                if j[0] in i and j[len(j)-1] in i:
                    moved = True
                    break
        # (10,20) - (5,15) -> (5,20)            
                elif j[0] in i and j[len(j)-1] not in i:
                    self.new_range[index] = range(i[0], j[len(j)-1]+1)
                    moved = True
                    break
        # (10,20) - (15,25) -> (10,25)
                elif j[0] not in i and j[len(j)-1] in i:
                    self.new_range[index] = range(j[0], i[len(i)-1]+1)
                    moved = True
                    break
        # (10,20) - (9,21) -> (9,21)
                elif j[0] < i[0] and j[len(j)-1] > i[len(i)-1]:
                    self.new_range[index] = j
                    moved = True
                    break
            
            if moved == False:
                self.new_range.append(j)
            else:
                found = True       
            
        return found 
    
def main() -> None:
    
    path = 'C:\\Users\\szita001\\Desktop\\advent\\2025_12_05.txt'
    
    day = day_05()
    
# Read input file
    with open(path, 'r') as file:
        for row in file:
            row = row.replace('\n', '')
            if '-' in row:
                ranges = row.split('-')             
                day.fresh_id_ranges.append(range(int(ranges[0]), int(ranges[1])+1 ))
            else:
                break
    
    while day.create_ranges():
        day.fresh_id_ranges = day.new_range[:]
        day.new_range.clear()
        
    print(f'The number of fresh ingredients: {day.get_number_of_ranges()}')
        
if __name__ == "__main__":
    main()