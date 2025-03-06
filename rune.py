class Rune:
    """
    Represents an input rune
    """

    def __init__(self, canvas):
        self.canvas = canvas        # Canvas to host the input rune
        self.lines = []             # Stores the ID of each line in the rune
        self.rune = []              # Stores which lines are enabled (1 if enabled, 0 otherwise)


    def toggle_line(self, line):
        """
        Toggles the provided line on or off

        :param line: ID of a line to toggle
        """
        if self.canvas.itemcget(line, "fill") == "black":
            self.canvas.itemconfigure(line, fill="gray75")
            self.rune[line - self.lines[0]] = 0
        else:
            self.canvas.itemconfigure(line, fill="black")
            self.rune[line - self.lines[0]] = 1


    def create_rune_line(self, start_x, start_y, end_x, end_y):
        """
        Draws a line to the rune's canvas and binds the necessary functions to it

        :param start_x: float, starting x-coordinate
        :param start_y: float, starting y-coordinate
        :param end_x: float, ending x-coordinate
        :param end_y: float, ending y-coordinate
        """
        new_line = self.canvas.create_line(start_x, start_y, end_x, end_y, width=8, fill="grey75")
        self.canvas.tag_bind(new_line, "<Button-1>", lambda x: self.toggle_line(new_line))

        self.lines.append(new_line)
        self.rune.append(0)


    def get_rune_string(self):
        """
        Returns this rune's array of enabled lines as a string

        :return: string
        """
        rune_string = "".join([str(i) for i in self.rune])
        return rune_string