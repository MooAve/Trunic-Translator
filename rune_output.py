class OutputRunes:

    def __init__(self, canvas):
        self.canvas = canvas
        self.cur_pos = 25


    def _add_outer_rune(self, rune, left, right):

        # TODO: Figure out a better way to check if a line is enabled
        #/\
        if rune[0] == "1":
            self.canvas.create_line(self.cur_pos, 5, left, 11.25, width = 2)
        if rune[1] == "1":
            self.canvas.create_line(self.cur_pos, 5, right, 11.25, width = 2)

        # ||
        if rune[2] == "1":
            self.canvas.create_line(left, 11.25, left, 36.25, width = 2)
        if rune[3] == "1":
            self.canvas.create_line(right, 11.25, right, 36.25, width = 2)

        # v
        if rune[4] == "1":
            self.canvas.create_line(left, 36.25, self.cur_pos, 42.5, width = 2)
        if rune[5] == "1":
            self.canvas.create_line(right, 36.25, self.cur_pos, 42.5, width = 2)


    def _add_inner_rune(self, rune, left, right):

        # W
        if rune[0] == "1":
            self.canvas.create_line(left, 11.25, self.cur_pos, 17.5, width = 2)
        if rune[1] == "1":
            self.canvas.create_line(self.cur_pos, 5, self.cur_pos, 17.5, width = 2)
        if rune[2] == "1":
            self.canvas.create_line(right, 11.25, self.cur_pos, 17.5, width = 2)

        # |
        if rune[3] == "1":
            self.canvas.create_line(self.cur_pos, 11.25, self.cur_pos, 25, width = 2)

        # M
        if rune[4] == "1":
            self.canvas.create_line(left, 36.25, self.cur_pos, 25, width = 2)
        if rune[5] == "1":
            self.canvas.create_line(self.cur_pos, 42.5, self.cur_pos, 25, width = 2)
        if rune[6] == "1":
            self.canvas.create_line(right, 36.25, self.cur_pos, 25, width = 2)


    def add_rune(self, outer_rune, inner_rune, circle):

        left = self.cur_pos - 6.25
        right = self.cur_pos + 6.25

        if outer_rune != "":
            self._add_outer_rune(outer_rune, left, right)
        if inner_rune != "":
            self._add_inner_rune(inner_rune, left, right)
        if circle:
            self.canvas.create_oval(left, 42.5, right, 55, width = 2)

        self.cur_pos += 12.5


    def add_space(self):
        self.cur_pos += 12.5

