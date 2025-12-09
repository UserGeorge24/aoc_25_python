
class day_07:
    
    def __init__(self):
        
        self.manifold = []
        self.count = 0
    
    def open_and_store(self):
        
        self.path = 'C:\\Users\\szita001\\Desktop\\advent\\2025_12_07.txt'
        
        with open(self.path, 'r') as file:
            for row in file:
                
                row = str(row.replace('\n', ''))
                self.manifold.append(row)
    
    def count_split(self):            

        search_indexes = []

        for index_i, i in enumerate(self.manifold):

            if index_i == 0:
                search_indexes.append(str(i).index('S'))

            looking_for_char = '^' if index_i != 0 else 'S'
            
            for index_j, j in enumerate(i):
                
                if j == looking_for_char and index_j in search_indexes:
                    
                # Char is found so can remove
                    search_indexes.remove(index_j)

                    if looking_for_char == 'S':
                        search_indexes.append(index_j)
                        break
                    
                    self.count += 1
                    
                # First char
                    if index_j != 0 and ( index_j - 1 ) not in search_indexes:
                        search_indexes.append(index_j - 1)    
                
                # Last char
                    if index_j != len(i) - 1 and ( index_j + 1 ) not in search_indexes:
                        search_indexes.append(index_j + 1)

def main() -> None:
    
    day = day_07()
    day.open_and_store()
    day.count_split()
    
    print(day.count)
        
if __name__ == "__main__":
    main()