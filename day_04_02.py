
class day_04:
    
    def __init__(self):
        self.rolls = []
        self.count = 0
        self.cons_rollsign = '@'
        self.rolls_found = 0
        self.indexes = []
    
    def get_rolls(self):
        return self.rolls
    
    def fill_rolls(self, rolls_string: str):
        self.rolls.append(rolls_string)
    
    def left_up_corner(self, x_coord, y_coord):
        
        # ?00
        # 0X0
        # 000
        
        new_y = y_coord - 1
        new_x = x_coord - 1
        
        if new_y >= 0 and new_x >= 0:
            try:
                if self.rolls[new_y][new_x] == self.cons_rollsign:
                    self.rolls_found += 1
            except IndexError:
                pass
        
    def left_value(self, x_coord, y_coord):

        # 000
        # ?X0
        # 000
        
        new_x = x_coord - 1
        if new_x >= 0:
            try:
                if self.rolls[y_coord][new_x] == self.cons_rollsign:
                    self.rolls_found += 1
            except IndexError:
                pass
        
    def left_down_corner(self, x_coord, y_coord):
        
        # 000
        # 0X0
        # ?00
        
        new_x = x_coord - 1     
        if new_x >= 0:
            try:
                if self.rolls[y_coord + 1][new_x] == self.cons_rollsign:
                    self.rolls_found += 1
            
            except IndexError:
                pass
        
    def down_value(self, x_coord, y_coord):
        
        # 000
        # 0X0
        # 0?0
        
        new_y = y_coord + 1
        
        try:
            if self.rolls[new_y][x_coord] == self.cons_rollsign:
                self.rolls_found += 1
        
        except IndexError:
            pass
        
    def right_down_corner(self, x_coord, y_coord):
        
        # 000
        # 0X0
        # 00?
        
        try:
            if self.rolls[y_coord + 1][x_coord + 1] == self.cons_rollsign:
                self.rolls_found += 1
        except IndexError:
            pass
        
    def right_value(self, x_coord, y_coord):
        
        # 000
        # 0X?
        # 000
        
        try:
            if self.rolls[y_coord][x_coord + 1] == self.cons_rollsign:
                self.rolls_found += 1
        except IndexError:
            pass
        
    def right_up_corner(self, x_coord, y_coord):
        
        # 00?
        # 0X0
        # 000
        
        new_y = y_coord - 1
        new_x = x_coord + 1
        
        if new_y >= 0: 
        
            try:
                if self.rolls[new_y][new_x] == self.cons_rollsign:
                    self.rolls_found += 1
            except IndexError:
                pass
        
    def up_value(self, x_coord, y_coord):
        
        # 0?0
        # 0X0
        # 000
        
        new_y_coord = y_coord - 1
        
        if new_y_coord >= 0:
            try:
                if self.rolls[new_y_coord][x_coord] == self.cons_rollsign:
                    self.rolls_found += 1
            except IndexError:
                pass
    
    def are_there_fewer_than_4_adj_rolls(self, x_coord, y_coord):
        
        self.rolls_found = 0

        self.left_up_corner(x_coord, y_coord)

        self.left_value(x_coord, y_coord)

        self.left_down_corner(x_coord, y_coord)

        self.down_value(x_coord, y_coord)
    
        self.right_down_corner(x_coord, y_coord)
            
        self.right_value(x_coord, y_coord)
            
        self.right_up_corner(x_coord, y_coord)
        
        self.up_value(x_coord, y_coord) 

        if self.rolls_found < 4: 
            self.indexes.append((y_coord, x_coord))
            
        return True if self.rolls_found < 4 else False
                
    def log_adjacent_rolls(self):
        self.count += 1
    
    def replace_values(self):
        for y_coord, x_coord in self.indexes:
            row = list(self.rolls[y_coord])
            row[x_coord] = '.'
            self.rolls[y_coord] = ''.join(row)          
        
        self.indexes = []  
            
    def scan_the_rolls(self):
        
        found = False
        
        for y_coord, rolls in enumerate(self.get_rolls()):
            for x_coord, roll in enumerate(rolls):
                if roll == self.cons_rollsign:
                    # print(day.get_rolls()[y_coord][x_coord])
                    if self.are_there_fewer_than_4_adj_rolls(x_coord, y_coord):
                        self.log_adjacent_rolls()
                        found = True
        
        self.replace_values()
        
        return found
            
def main() -> None:
    
    path = 'C:\\Users\\szita001\\Desktop\\advent\\2025_12_04.txt'
    
    day = day_04()
    
# Read input file
    with open(path, 'r') as file:
        for rolls in file:
            rolls = rolls.replace('\n', '')
            day.fill_rolls(rolls)

# Process rolls

    while day.scan_the_rolls():
        pass

    print(f"Number of rolls with fewer than 4 adjacent rolls: {day.count}")
    
    # print("Modified rolls:")
    # for rolls in day.get_rolls():
        # print(rolls)
    
if __name__ == "__main__":
    main()