


def main() -> None:
    
    path = 'C:\\Users\\szita001\\Desktop\\advent\\2025_12_03.txt'
    
    joltages = []

    with open(path, 'r') as file:
        for row in file:
            
            row = row.replace('\n', '')
            
            index_of_max = row.index(max(row))
            
            if len(row) != index_of_max + 1:
                
                joltage = int( str( row[index_of_max] ) + str( max(row[index_of_max+1:]) ) ) 
                joltages.append(joltage)
                
            else:
                
                joltage = int( str(max(row[:index_of_max])) + str(row[index_of_max]) )
                joltages.append(joltage)
                

    print( sum(joltages) )

if __name__ == "__main__":
    main()