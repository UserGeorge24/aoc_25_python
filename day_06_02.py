
class day_06:
    
    def __init__(self):
        
        self.math = []
        self.signs = []
        self.path = 'C:\\Users\\szita001\\Desktop\\advent\\2025_12_06.txt'
        self.unconverted_numebrs = []
        self.group_by_calc = 0
        self.all_sum = 0
    
    def open_and_store(self):
        
        with open(self.path, 'r') as file:
            for row in file:
                
                row = row.replace('\n', '')
                self.unconverted_numebrs.append(row)
                
    def convert_numbers(self):
        
        self.group_by_calc = len(self.unconverted_numebrs) - 1
        
        for i in self.unconverted_numebrs:
            
            for index, j in enumerate(i):
        
                if j != '+' and j != '*':
                    try:
                        self.math[index] = self.math[index] + str(j)
                    except IndexError:
                        self.math.insert(index, str(j))
                else:             
                    try:
                        
                        if '+' in i[index+1:]:
                            next_plus_index = i[index+1:].index('+')
                        else:
                            next_plus_index = 0
                        
                        if '*' in i[index+1:]:
                            next_multi_index = i[index+1:].index('*')
                        else:
                            next_multi_index = 0
                        
                        if next_plus_index != 0 and next_multi_index != 0:
                            next_sign_index = next_plus_index if next_plus_index < next_multi_index else next_multi_index
                        
                        elif next_plus_index != 0:
                            next_sign_index = next_plus_index
                        
                        elif next_multi_index != 0:
                            next_sign_index = next_multi_index
                            
                        else:
                            next_sign_data  = [str(j), len(i[index+1:])+1 ]
                            self.signs.append(next_sign_data)
                            break
                        
                        next_sign_data  = [str(j), next_sign_index ]
                        self.signs.append(next_sign_data)
                    except ValueError:
                        pass
                        
#   cleaning up the numbers from strings to integers
        self.math = [ int(str(i).strip()) for i in self.math if str(i).strip().isnumeric() ]
        self.math.insert(len(self.math), '')
    
    def calc_result(self):

        index_from = 0
        index_to = 0
        temp_values = []

        for value in self.signs:
            
            index_to    += value[1]
            temp_values =  self.math[index_from:index_to]
            
            if value[0] == '+':
                self.all_sum += sum(temp_values)
            else:
                temp = 1
                try:
                    for j in temp_values:
                        temp *= j

                    self.all_sum += temp
                except Exception:
                    pass
            
            temp_values.clear()
            index_from = index_to
            
def main() -> None:
    
    day = day_06()
    day.open_and_store()
    day.convert_numbers()
    day.calc_result()
    
    print(day.all_sum)
        
if __name__ == "__main__":
    main()