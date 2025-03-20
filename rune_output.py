class OutputRunes:

    def __init__(self, canvas):
        self.canvas = canvas
        self.cur_pos = 25

    def add_rune(self, outer_rune = "", inner_rune = ""):

        left = self.cur_pos - 6.25
        right = self.cur_pos + 6.25

        # TODO: Figure out a better way to check if a rune is enabled

        #/\
        if outer_rune[0] == "1":
            self.canvas.create_line(self.cur_pos, 5, left, 11.25, width = 2)
        if outer_rune[1] == "1":
            self.canvas.create_line(self.cur_pos, 5, right, 11.25, width = 2)

        # ||
        if outer_rune[2] == "1":
            self.canvas.create_line(left, 11.25, left, 26.25, width = 2)
        if outer_rune[3] == "1":
            self.canvas.create_line(right, 11.25, right, 26.25, width = 2)

        # v
        if outer_rune[4] == "1":
            self.canvas.create_line(left, 26.25, self.cur_pos, 32.5, width = 2)
        if outer_rune[4] == "1":
            self.canvas.create_line(right, 26.25, self.cur_pos, 32.5, width = 2)

        self.cur_pos += 12.5


    def add_space(self):
        self.cur_pos += 12.5

