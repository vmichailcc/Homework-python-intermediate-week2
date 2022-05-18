class ReverseIter:
    def __init__(self, input_list):
        self.input_list = input_list

    def revers_itetation(self):
        for value in reversed(self.input_list):
            print(value)


list1 = [x for x in range(12)]
t = ReverseIter(list1)
t.revers_itetation()
