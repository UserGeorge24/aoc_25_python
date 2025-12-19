
class day_09:
    
    def __init__(self):
        
        self.coords = []
        self.max_area = 0
        
    def open_and_store(self):
        
        self.path = 'C:\\Users\\szita001\\Desktop\\advent\\2025_12_09.txt'
        
        with open(self.path, 'r') as file:
            for row in file:
                row = list(str(row.replace('\n', '')).split(','))
                row = [ int(i) for i in row ]
                self.coords.append(row)

    def calc_area(self,a,b):
        
        c = abs(b[0]-a[0])+1
        d = abs(b[1]-a[1])+1
        
        return c*d
    
    def find_biggest_area(self):
        
        for i in range(len(self.coords)):
            for j in range(1,len(self.coords)):

                if self.max_area < self.calc_area(self.coords[i],self.coords[j]):
                    self.max_area = self.calc_area(self.coords[i],self.coords[j])
                
def main() -> None:
    
    day = day_09()
    day.open_and_store()
    day.find_biggest_area()

    print(f'Max area: {day.max_area}')

if __name__ == "__main__":
    main()