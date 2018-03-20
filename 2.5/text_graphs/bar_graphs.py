class BarGraphDrawer:
  """A class that draws horizontal bar graphs from data.

  TODO: Make this draw bar graphs vertically, but that's harder.
  """

  def __init__(self):
    pass

  def draw_bar_graph(self, data):
    for number in data:
      print(" |" + ("*" * number))


