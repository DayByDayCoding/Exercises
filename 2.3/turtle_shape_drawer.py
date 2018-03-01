import turtle


class TurtleShapeDrawer:
  """A class of convenient methods for drawing shapes with a turtle."""

  def __init__(self, color):
    self.color = color
    turtle.fillcolor(color)

  def draw_rectangle(self, rectangle):
    """Draws the given RectangleToDraw on screen.

    Args:
      rectangle: a RectangleToDraw object
    """
    turtle.penup()
    turtle.setpos(rectangle.x1, rectangle.y1)
    turtle.pendown()
    turtle.begin_fill()
    turtle.setpos(rectangle.x2, rectangle.y1)
    turtle.setpos(rectangle.x2, rectangle.y2)
    turtle.setpos(rectangle.x1, rectangle.y2)
    turtle.setpos(rectangle.x1, rectangle.y1)
    turtle.penup()
    turtle.end_fill()

  def stay_on_screen(self):
    """Called after all shapes have been drawn, to keep the window open.

    This really just calls turtle.done(), but I didn't want users of this class
    to have to call "raw" turtle functions on their own.
    """
    turtle.done()



class RectangleToDraw:
  """Represents a rectangle as upper-left and lower-right x-y coordinates"""

  def __init__(self, x1, y1, x2, y2):
    self.x1 = x1
    self.y1 = y1
    self.x2 = x2
    self.y2 = y2




drawer = TurtleShapeDrawer("red")

rect = RectangleToDraw(-100, 80, 150, -190)
drawer.draw_rectangle(rect)

drawer.stay_on_screen()

