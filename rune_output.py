class OutputRunes:
    """
    Class used to hold all the previously inputted runes
    Requires a canvas object
    """

    def __init__(self, canvas):
        self.canvas = canvas
        self.cur_pos = 25
        self.cur_runes = []


    def _add_outer_rune(self, rune, left, right):
        """
        Helper function for "add_rune"
        Creates the necessary lines for the outer rune

        :param rune: String displaying which lines are enabled
        :param left: Leftmost x-coordinate for creating rune lines
        :param right: Rightmost x-coordinate for creating rune lines
        """

        # Maybe Figure out a better way to check if a line is enabled
        #/\
        if rune[0] == "1":
            self.canvas.create_line(self.cur_pos, 5, left, 11.25, width = 2)
        if rune[1] == "1":
            self.canvas.create_line(self.cur_pos, 5, right, 11.25, width = 2)

        # |
        if rune[2] == "1":
            self.canvas.create_line(left, 11.25, left, 36.25, width = 2)

        # v
        if rune[3] == "1":
            self.canvas.create_line(left, 36.25, self.cur_pos, 42.5, width = 2)
        if rune[4] == "1":
            self.canvas.create_line(right, 36.25, self.cur_pos, 42.5, width = 2)


    def _add_inner_rune(self, rune, left, right):
        """
        Helper function for "add_rune"
        Creates the necessary lines for the inner rune

        :param rune: String displaying which lines are enabled
        :param left: Leftmost x-coordinate for creating rune lines
        :param right: Rightmost x-coordinate for creating rune lines
        """

        # W
        if rune[0] == "1":
            self.canvas.create_line(left, 11.25, self.cur_pos, 17.5, width = 2)
        if rune[1] == "1":
            self.canvas.create_line(self.cur_pos, 5, self.cur_pos, 17.5, width = 2)
        if rune[2] == "1":
            self.canvas.create_line(right, 11.25, self.cur_pos, 17.5, width = 2)

        # |
        if rune[3] == "1":
            self.canvas.create_line(self.cur_pos, 17.5, self.cur_pos, 25, width = 2)

        # M
        if rune[4] == "1":
            self.canvas.create_line(left, 36.25, self.cur_pos, 25, width = 2)
        if rune[5] == "1":
            self.canvas.create_line(self.cur_pos, 42.5, self.cur_pos, 25, width = 2)
        if rune[6] == "1":
            self.canvas.create_line(right, 36.25, self.cur_pos, 25, width = 2)


    def add_rune(self, outer_rune, inner_rune, circle):
        """
        Adds a rune to the output canvas

        :param outer_rune: String representing the outer rune
        :param inner_rune:  String representing the inner rune
        :param circle: Bool, creates the rune circle if true
        """

        left = self.cur_pos - 6.25
        right = self.cur_pos + 6.25

        if outer_rune != "00000":
            self._add_outer_rune(outer_rune, left, right)
        if inner_rune != "0000000":
            self._add_inner_rune(inner_rune, left, right)

        if circle:
            self.cur_runes.append(outer_rune)
            self.cur_runes.append(inner_rune)
            self.canvas.create_oval(left - .5, 42.5, right - .5, 55, width = 2)
        else:
            self.cur_runes.append(inner_rune)
            self.cur_runes.append(outer_rune)

        self.cur_pos += 12.5


    def add_space(self):
        """
        Adds a blank space to the output canvas
        """

        self.cur_runes.append("_")
        self.cur_pos += 12.5


    def delete_rune(self):
        """
        Deletes the last rune added to the output canvas
        """

        # Do not move the current position if there are no runes to delete
        if self.cur_pos == 25:
            return

        self.cur_pos -= 12.5

        last_rune = self.canvas.find_overlapping(self.cur_pos - 5.25, 0, self.cur_pos + 5.25, 100)

        for line in last_rune:
            self.canvas.delete(line)

        # Remove inner/outer rune pair from list if it was not a space
        if self.cur_runes.pop() != "":
            self.cur_runes.pop()


    def clear_all_runes(self):
        """
        Deletes all previously inputted runes
        """

        self.cur_runes.clear()

        self.cur_pos = 25
        self.canvas.delete("all")


    def get_output_runes(self):
        """
        Returns a list of saved output runes
        :return:  list of strings representing output runes
        """

        return self.cur_runes


    def set_output_runes(self, new_runes):
        """
        Sets the current output runes to the provided list
        Resets the current list of output runes
        :param new_runes: A list of strings representing output runes
        """

        self.clear_all_runes()

        i = 0

        while i < len(new_runes):
            if new_runes[i] != "_":
                # Check rune lengths to determine if a circle should be added
                # If an invalid rune is found, stop loading runes and clear previously loaded ones
                if len(new_runes[i]) == 5 and len(new_runes[i + 1]) == 7:
                    self.add_rune(new_runes[i], new_runes[i + 1], True)
                elif len(new_runes[i]) == 7 and len(new_runes[i+1]) == 5:
                    self.add_rune(new_runes[i + 1], new_runes[i], False)
                else:
                    print("ERROR: Invalid Rune In File")
                    self.clear_all_runes()
                    return
                i += 2
            else:
                self.add_space()
                i += 1