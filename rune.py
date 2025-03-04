class Rune:
    canvas = None

    def __init__(self, canvas):
        self.canvas = canvas
        self.lines = []
        self.rune = []


    def toggle_line(self, line):
        if self.canvas.itemcget(line, "fill") == "black":
            self.canvas.itemconfigure(line, fill="gray75")
            self.rune[line - self.lines[0]] = 0
        else:
            self.canvas.itemconfigure(line, fill="black")
            self.rune[line - self.lines[0]] = 1


    def create_rune_line(self, start_x, start_y, end_x, end_y):
        new_line = self.canvas.create_line(start_x, start_y, end_x, end_y, width=8, fill="grey75")
        self.canvas.tag_bind(new_line, "<Button-1>", lambda x: self.toggle_line(new_line))

        print("Adding new line: " + str(new_line))

        self.lines.append(new_line)
        self.rune.append(0)


    def get_rune_string(self):
        rune_string = "".join([str(i) for i in self.rune])
        return rune_string