import matplotlib.pyplot as plt
import numpy as np
"""
I, Ali Abubaker 000857347 certify that this material is my original", "work. I have not shared this file. No other person's work has been used without due acknowledgement.
"""
# Provided Information
in1 = [1139, 1169, 1206, 1254, 1294, 1310, 1328, 1378, 1383, 1306, 1467,
        1501,1533, 1532, 1576, 1601, 1661, 1674, 1751, 1827, 1891]
cpi = [103, 105, 107, 109, 112, 114, 114, 116, 120, 122, 123, 125, 127,
        128,130, 133, 136, 137, 142, 151, 157]
in2 = [1012, 1029, 1078, 1097, 1152, 1211, 1253, 1368, 1352, 1408, 1483, 1527,
    1545, 1517, 1520, 1577, 1633, 1670, 1744, 1798, 1964]
years = np.arange(2003, 2024)
# Take inflation into account.
def adjust_for_inflation(values, cpi):
    return [v * (cpi[-1] / cpi[i]) for i, v in enumerate(values)]
in1_adj, in2_adj = adjust_for_inflation(in1, cpi), adjust_for_inflation(in2, cpi)
middle_value_in1, middle_value_in2 = np.median(in1_adj), np.median(in2_adj)
# Addition of horizontal lines function
def add_horizontal_lines(ax, mid1, mid2, color1, color2, style1, style2):
    ax.axhline(y=mid1, color=color1, linestyle=style1)
    ax.axhline(y=mid2, color=color2, linestyle=style2)
# Create Subplots
fig, axes = plt.subplots(2, 2, figsize=(8, 6))
plt.subplots_adjust(hspace=0.4, wspace=0.4)
# Line and bar chart plotting functions
def plot(ax, title, color1, color2, style1, style2, width, is_bar=False):
    if is_bar:
        ax.bar(years, in1_adj, label="Computer systems design and related services [5415]",
         color=color1, alpha=0.7)
        ax.bar(years - 0.2, in2_adj, label="Scientific research and development services [5417]",
         color=color2, alpha=0.7)
        # Make a bar chart with horizontal lines.
        add_horizontal_lines(ax, middle_value_in1, middle_value_in2, color1,
        color2, style1, style2)
    else:
        ax.plot(years, in1_adj, label="Computer systems design and related services [5415]",
         color=color1,
                linestyle=style1, linewidth=width)
        ax.plot(years, in2_adj, label="Scientific research and development services [5417]",
         color=color2,
                linestyle=style2, linewidth=width)
        # To the line graph, add horizontal lines.
        add_horizontal_lines(ax, middle_value_in1, middle_value_in2, color1,
         color2, style1,style2)
    ax.set_title(title, fontsize=8)
    ax.set_xlabel("Year (2000s)", fontsize=10)
    ax.set_ylabel("Weekly Income (adjusted to 2023 CAD)", fontsize=8)
    ax.set_ylim(900, 2300)
    ax.set_yticks([1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900,
     2000, 2100,2200])
    ax.set_xticklabels([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24])
    ax.set_xticks([2002, 2004, 2006, 2008, 2010, 2012, 2014, 2016, 2018, 2020,
     2022, 2024])
    ax.legend(fontsize=6)
# Plot the graphs, then for each plot, add horizontal lines.
plot(axes[0, 0], "Weekly Incomes By Occupation (line Graph)", 'b', 'c', '--', '-', 2)
plot(axes[0, 1], "Weekly Incomes By Occupation (line Graph)", 'g', 'y', '-', '--', 3)
plot(axes[1, 0], "Weekly Incomes By Occupation (Bar Graph)", 'b', 'brown', ':', ':', 0,
 is_bar=True)
plot(axes[1, 1], "Weekly Incomes By Occupation (Bar Graph)", 'g', 'y', '-', '-', 0,
 is_bar=True)
# Save and Show
plt.savefig("a1_Abubaker_000857347.png", dpi=100)
plt.show()
