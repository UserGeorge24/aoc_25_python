
class day_06:
    
    def __init__(self):
        
        self.math = []
        self.results = []
        self.signs = []
        self.path = 'C:\\Users\\szita001\\Desktop\\advent\\2025_12_06.txt'
    
    def open_and_store(self):
        
        with open(self.path, 'r') as file:
            for index, row in enumerate(file):
                
                row = row.replace('\n', '')
                temp = row.split(' ')
                temp = list(filter(lambda x: x != '', temp))
                
                try:
                    temp = [int(i) for i in temp]
                    self.math.append(temp)
                except ValueError:
                    self.signs = temp        
    
    def calc_result(self):

        for i in self.math:
            if self.results != []:
                for index, j in enumerate(self.signs):
                    try:                    
                        if j == '+':
                            self.results[index] += int(i[index])
                        else:
                            self.results[index] *= int(i[index])
                    except IndexError:
                        pass
            else:
                self.results = i[:]        
    
def main() -> None:
    
    day = day_06()
    
# Read input file

    day.open_and_store()
    
    day.calc_result()
    
    print(sum(day.results))
        
if __name__ == "__main__":
    main()