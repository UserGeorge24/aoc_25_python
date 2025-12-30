class day_10:
    
    def __init__(self):
        
        self.machines = []
        self.sum_presses = 0
        
    def open_and_store(self):
        
        self.path = 'C:\\Users\\szita001\\Desktop\\advent\\2025_12_10.txt'
        
        with open(self.path, 'r') as file:
            for row in file:
                row = list(str(row.replace('\n', '')).split(' '))
                
                row[0] = row[0].replace('[','')
                row[0] = row[0].replace(']','')
                
                for i in range(len(row[1:-1])):
                    row[i+1] = row[i+1].replace('(','')
                    row[i+1] = row[i+1].replace(')','')
                        
                row[-1] = row[-1].replace('{','')
                row[-1] = row[-1].replace('}','')
               
                content = []
                content.insert(0, row[0])
                content.insert(2,row[-1])
                content.insert(1, row[1:-1])
                
                self.machines.append(content)

    def do(self):
        
        for i in self.machines:
            
            states = []
            press_count = 0
            done = False
            
            # Convert target state to binary string
            target_state = ''.join([ '1' if j == '#' else '0' for j in i[0] ])
            init_state = len(i[0]) * '0'
            button_states = []
            states.append(init_state)
            
            self.generate_binary_state(i[1], button_states, init_state)
                  
            while True:
                
                temp = []
                press_count += 1
                
                for j in button_states:
                    for k in states:
                        if k != j:
                            # XOR operation
                            
                            result = bin(int(j,2) ^ int(k,2)).replace('0b','').zfill(len(i[0]))
                            
                            if result not in temp:
                                temp.append(result)
                            
                            if target_state == temp[-1]:
                                self.sum_presses += press_count
                                done = True
                                break
                    if done:
                        break
                if done:
                    break
                else:
                    states = temp                        

    def generate_binary_state(self, buttons, states, init_state):
        
        state = str() 
        
        for j in buttons:
            state = init_state
            for k in str(j).replace(',', ''):
                state = state[:int(k)] + '1' + state[int(k)+1:]
                
            states.append(state)

def main() -> None:
    
    day = day_10()
    day.open_and_store()
    day.do()
    
    print(day.sum_presses)

if __name__ == "__main__":
    main()