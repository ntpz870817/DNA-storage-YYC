"""
Name: Progress Monitor

Coder: HaoLing ZHANG (BGI-Research)[V1]

Current Version: 1

Function(s):
Get the progress and the time left
"""

from datetime import datetime


class Monitor:

    def __init__(self):
        """
        introduction: Restore monitor settings.
        """
        self.position = 0
        self.last_time = datetime.now()

    def restore(self):
        """
        introduction: Restore monitor settings.
        """
        self.__init__()

    def output(self, current_length, total_length, extra_informs=None):
        """
        introduction: Print the progress bar for required "for" sentence.

        :param current_length: Current position of the "for" sentence. (int)
        :param total_length: Total length of the "for" sentence. (int)
        :param extra_informs: extra information in the specific tasks. ()
        """
        position = round(current_length / total_length * 100)

        self.position = position
        string = "["
        for index in range(100):
            if position > index:
                string += "|"
            else:
                string += " "
        string += "]"

        time_left = (datetime.now() - self.last_time).total_seconds()

        if extra_informs is None:
            string += "(detect = " + str(current_length) + ", total = " + str(total_length) + ") "
        else:
            string += "(detect = " + str(current_length) + ", {"
            for index, extra_inform in enumerate(extra_informs):
                string += extra_inform[0] + " = " + extra_inform[1]
                if index < len(extra_informs) - 1:
                    string += ", "
            string += "}, total = " + str(total_length) + ") "
        if self.position < 100:
            string += str(position) + "%, will be completed in " + str(
                round(time_left * (100 - position) / (position + 1), 2)) + " seconds."
        else:
            string += str(position) + "%, was spent " + str(round(time_left, 2)) + " seconds."

        print("\r" + string, end=" ")

        if current_length == total_length:
            print()
