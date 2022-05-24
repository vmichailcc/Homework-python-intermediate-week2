class ReverseIter:
    def __init__(self, input_list):
        self.input_list = input_list

    def __iter__(self):
        self.a = 0
        self.b = -1
        return self

    def __next__(self):
        if self.a < len(self.input_list):
            output_list = self.input_list[self.b]
            self.a += 1
            self.b -= 1
            return output_list
        else:
            raise StopIteration


list1 = [x for x in range(12)]
for i in ReverseIter(list1):
    print(i)
