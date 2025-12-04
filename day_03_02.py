

def main() -> None:
    
    path = 'C:\\Users\\szita001\\Desktop\\advent\\2025_12_03.txt'
    
    joltages = []
    
    with open(path, 'r') as file:
        for row in file:
            
            row = row.replace('\n', '')
            
            finished = False
            index = 0
            
            while not finished:
                
                try:
                    if row[index] < row[index+1]:    
                        row = row[:index] + row[index+1:]
                        index = 0
                    elif row[index] == row[index+1] and index != 0:
                        
                        next_min = min(row[index:])
                        if row[index] < next_min:
                            row = row[:index] + row[index+1:]
                            index = 0
                        else:
                            index += 1   
                    else:
                        index += 1
                
                except IndexError:
                    print(row[:12])
                    joltages.append(int(row[:12]))
                    finished = True                      
                        
                if len(row) == 12:
                    print(row)
                    joltages.append(int(row))
                    finished = True
                elif row[:12] == '999999999999':
                    print(row[:12])
                    joltages.append(int(row[:12]))
                    finished = True


    print( 'sum: ' + str(sum(joltages)) )
    
if __name__ == "__main__":
    main()