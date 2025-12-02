from day_02_01 import day_02, main

class day_02_02(day_02):

    def find_invalid_ids(self, ranges):

       for i in range(ranges[0],ranges[1] + 1):
#       work with unmatched numbers only          
            i = str(i)

            finished = False
            index = 0

            if len(i) > 1:

                while not finished:

    #               stop condition for even numbers if the program reach the middle of the string
                    if len(str(i)) % 2 == 0 and index == ( len(i) // 2 ):
                        finished = True
                        continue

                    if len(str(i)) % 2 != 0 and index > round( len(i) // 3 ):
                        finished = True
                        continue

                    index += 1

                    pattern = i[0:index]
                    occurence = i.count(pattern)

                    if len(i) == occurence * len(pattern):
                        self.invalid_ids.append(i)
                        finished = True

def main() -> None:
   
    path = 'src_02'

    object = day_02_02()

    with open(path, 'r') as file:
        for row in file:
            object.separate_ranges(row.replace('\n',''))

    for range in object.ranges:
            object.find_invalid_ids(range)

    print(f'Sum of Invalid IDs: {sum(int(i) for i in object.invalid_ids)}')

if __name__ == "__main__":
    main()