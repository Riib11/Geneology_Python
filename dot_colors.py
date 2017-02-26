# range 0+
colors = ["red","black", "cyan","indigo", "blue", "green", "purple", "tan", "darkgreen"]
def num_to_color(num):
    if num > len(colors) or num < 0:
        return 1
    return colors[num]