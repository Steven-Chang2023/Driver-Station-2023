class Button:
    isClicked = False

    def __init__(self, tag, x, y, width, height, text, color="blue", font_size=18):
        # Set name, dimensions and text
        self.name = tag
        self.height = height
        self.width = width
        self.x1 = x
        self.x2 = x + width
        self.y1 = y
        self.y2 = y + height
        self.wdith = width
        self.height = height
        self.text = text
        self.text_active = text
        self.color = color
        self.font_size = font_size
    
    def drawButton(self, ctx):
        # Create the actual button
        ctx.delete(self.name)
        ctx.create_rectangle(self.x1, self.y1, self.x2, self.y2, tag=self.name, fill=self.color)

        # Create the text on the button
        ctx.delete(self.name+"text")
        ctx.create_text(self.x1+(self.width/2), self.y1+(self.height/2), 
            text=self.text_active, tag=self.name+"_text", font = ("Arial", self.font_size))

    def checkClicked(self, event):
        # If the click is inside the rectange of the button, it is clicked
        if (event.x >= self.x1 and event.x <= self.x2) and (event.y >= self.y1 and event.y <= self.y2):
            self.isClicked = True
        else:
            self.isClicked = False

