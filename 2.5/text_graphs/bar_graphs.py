import graph_config


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


# DBDC students: Wondering what this __main__ thing is all about?
# Google it, or wait for a later video to explore this...
if __name__ == "__main__":
  config = graph_config.GraphConfig("m", 2)
  drawer = BarGraphDrawer(config)
  drawer.draw_bar_graph([3, 4, 5, 9, 4, 2, 1, 2])

