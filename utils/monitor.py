class Monitor:
    def __init__(self):
        self.position = -1

    def restore(self):
        self.position = -1

    def print(self, current_length, total_length):
        position = int(current_length / total_length * 100)

        if self.position < position:
            self.position = position
            string = "["
            for index in range(100):
                if position + 1 > index:
                    string += "|"
                else:
                    string += " "
            string += "]  "
            if 10 < self.position + 1 < 100:
                string += " "
            elif self.position + 1 < 10:
                string += "  "

            print("\r" + string + str(position + 1) + "%", end=" ")
            if self.position + 1 >= 100:
                print()
