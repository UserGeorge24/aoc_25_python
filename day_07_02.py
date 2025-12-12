
class day_07:
    
    def __init__(self):
        
        self.manifold = []
    
    def open_and_store(self):
        
        self.path = 'C:\\Users\\szita001\\Desktop\\advent\\2025_12_07.txt'
        
        with open(self.path, 'r') as file:
            for row in file:
                
                row = str(row.replace('\n', ''))
                self.manifold.append(row)
    
    def convert_manifold_to_array(self):
        
        array = []
        
        for i in self.manifold:
            row = []
            for j in i:
                if j == 'S':
                    j = 1
                elif j == '.':
                    j = 0
                elif j == '^':
                    j = -1
                
                row.append(j)
            array.append(row)
        self.manifold = array
           
    def count_routes(self):
        for i in range(1,len(self.manifold[0])):
            for j in range(len(self.manifold[0])):
                
                if self.manifold[i][j] >= 0:
                    self.manifold[i][j] += self.manifold[i-1][j]
                elif self.manifold[i][j] == -1:
                    self.manifold[i][j] = 0
                    self.manifold[i][j-1] += self.manifold[i-1][j]
                    self.manifold[i][j+1] += self.manifold[i-1][j]        
           
def main() -> None:
    
    day = day_07()
    day.open_and_store()
    day.convert_manifold_to_array()
    day.count_routes()
       
    print(sum(day.manifold[-2]))
       
if __name__ == "__main__":
    main()