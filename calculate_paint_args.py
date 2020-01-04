# calculating how many litres of paint you need
def calculate_paint(efficency_ltr_per_m2, *args):
    total_area = sum(args)
    return efficency_ltr_per_m2 * total_area


print(calculate_paint(0.5, 10, 15, 9, 12))
rooms = [10, 15, 9, 12]
print(calculate_paint(0.5, *rooms))
