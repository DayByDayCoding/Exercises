import text_graphs
import text_graphs.graph_config
import text_graphs.line_graphs
import text_graphs.bar_graphs

line_config = text_graphs.graph_config.GraphConfig("y", 4)
line_drawer = text_graphs.line_graphs.LineGraphDrawer(line_config)
line_drawer.draw_line_graph([3, 4, 5, 7, 4, 2, 1, 7])

print()
print()
print("BAR GRAPH:")
print()

bar_config = text_graphs.graph_config.GraphConfig("&", 3)
bar_drawer = text_graphs.bar_graphs.BarGraphDrawer(bar_config)
bar_drawer.draw_bar_graph([2, 14, 6, 7, 8, 0, 9])

