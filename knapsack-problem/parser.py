def read_file(file):

    file = open(file, "r")
    lines = file.readlines()
    items = []
    number_items, total_weight = lines[0].strip('\n').split(' ')
    for line in lines[1:]:
        profit, weight = line.strip('\n').split(' ')
        items.append((float(profit), float(weight)))
    return items, float(total_weight)
