# range 0+
colors = ["cyan","black", "red","indigo", "blue", "green", "purple", "tan", "darkgreen"]
def num_to_color(num):
    if num > len(colors) or num < 0:
        return 1
    return colors[num]