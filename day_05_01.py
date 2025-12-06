
class day_05:
    
    def __init__(self):
        
        self.ingredeints = []
        self.fresh_id_ranges = []
        self.fresh_ingredients = 0
    
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
                if row != '':        
                    day.ingredeints.append(int(row))
    
    # day.fresh_id_ranges.sort()
    day.ingredeints.sort()
    
    for i in day.ingredeints :
        
        for j in day.fresh_id_ranges:
        
            if i in j:
                day.fresh_ingredients += 1
                print(f'Fresh ID found: {i}')
                break
    
    print(f'The number of fresh ingredients is: {day.fresh_ingredients}')
    
if __name__ == "__main__":
    main()