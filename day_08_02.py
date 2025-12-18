
import math

class day_07:
    
    def __init__(self):
        
        self.coords = []
        self.distances = []
        self.circuits = []
        self.count = 1
        
    def open_and_store(self):
        
        self.path = 'C:\\Users\\szita001\\Desktop\\advent\\2025_12_08.txt'
        
        with open(self.path, 'r') as file:
            for row in file:
                row = str(row.replace('\n', ''))
                temp = list(row.split(','))
                temp = [ int(i) for i in temp ]
                self.coords.append(temp)

    def calc_distance(self):
        
        for i in range(len(self.coords)):
            for j in range(i+1,len(self.coords)):
                distance = math.hypot(self.coords[j][0] - self.coords[i][0], \
                                      self.coords[j][1] - self.coords[i][1], \
                                      self.coords[j][2] - self.coords[i][2]  )
                
                self.distances.append([self.coords[i], self.coords[j], distance])

        self.distances.sort(key = lambda x: x[-1])

    def sum_circuits(self):
        
        # sort sel.circuits by length of their elements
        self.circuits.sort(key = lambda x: len(x), reverse=True)        
        
        for i in range(3):
            self.count *= len(self.circuits[i])
            
    def find_circuits(self, connection_limit):
        
        for i in range(0,connection_limit):

            value = self.distances[i]

        # Does it exists in one of the circuit?

            index_x = -1
            index_y = -1

            for index_j, j in enumerate(self.circuits):
                if value[0] in j:
                    index_x = index_j
                
                if value[1] in j:
                    index_y = index_j

        # Both of them are connected to different than merge them
            if index_y != -1 and index_x != -1 and index_y != index_x:
                for k in self.circuits[index_y]:
                    self.circuits[index_x].append( k )
                self.circuits.pop(index_y)
                continue
            elif index_y != -1 and index_x != -1 and index_y == index_x:
                continue
            
        # One of them is connect to circuit, other them can be added    
            if index_x != -1:
                self.circuits[index_x].append(value[1])
            
        # One of them is connect to circuit, other them can be added
            elif index_y != -1:
                self.circuits[index_y].append(value[0])
            
        # Both them are add
            else:
                self.circuits.append([value[0],value[1]])
            
            if len(self.circuits[0]) == len(self.coords):
                print(value[0][0]*value[1][0])
                break
            
def main() -> None:
    
    day = day_07()
    day.open_and_store()
    day.calc_distance()
    day.find_circuits(len(day.distances)-1)
    # day.sum_circuits()
    
    # print(day.count)

if __name__ == "__main__":
    main()