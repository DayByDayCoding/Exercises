class BarGraphDrawer:
  """A class that draws horizontal bar graphs from data.

  TODO: Make this draw bar graphs vertically, stealing the line approach?
  """

  def __init__(self, config):
    self.config = config

  def draw_bar_graph(self, data):
    spacing = " " * (self.config.width_spacing - 1)
    spaced_symbol = spacing + self.config.point_symbol
    for number in data:
      print("|" + (spaced_symbol * number))

