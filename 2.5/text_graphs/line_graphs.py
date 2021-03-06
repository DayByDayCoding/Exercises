class LineGraphDrawer:
  """A class that draws line graphs from data."""

  def __init__(self, config):
    self.config = config

  def assemble_data_dict(self, data):
    idx = 0
    assembled = {}
    for number in data:
      if (number not in assembled):
        assembled[number] = []
      assembled[number].append(idx)
      idx += 1
    return assembled

  def draw_line_graph(self, data):
    assembled = self.assemble_data_dict(data)
    #print("assembled result:", assembled)

    sorted_keys = sorted(assembled.keys(), reverse=True)
    row_width = len(data)
    chart_height = sorted_keys[0]

    for row_number in range(chart_height, 0, -1):
      row_string = [" "] * row_width

      if (row_number in assembled):
        for column_number in assembled[row_number]:
          row_string[column_number] = self.config.point_symbol

        spacing = " " * (self.config.width_spacing - 1)
        print("|" + spacing.join(row_string))
      else:
        print("|")

    # Bottom row
    print("└" + ("-" * row_width * self.config.width_spacing))



# (old notes) The plan:
# ex: [2, 20, 5]
# { 0: 2, 1: 20, 2: 5 }
# more like: { 2: 0, 20: 1, 5: 2 }
# then sort: { 20: 1, 5: 2, 2: 0 }


