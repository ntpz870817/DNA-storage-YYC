import utils.log as log


class Monitor:
    def __init__(self):
        self.position = -1

    def restore(self):
        self.position = -1

    def print(self, current_length, total_length, step_proportion):
        position = int(current_length / total_length * step_proportion * 100)

        if self.position < position:
            self.position = position
            string = ""
            for index in range(100):
                if position > index:
                    string += "|"
                else:
                    string += " "
            log.output(log.NORMAL, "", "", string + str(position + 1) + "%.")
