def mean(*args):
    return sum(args) / len(args)

def variance_sample(*args):
    avg = sum(args) / len(args)
    deviation = 0
    for i in args:
        deviation += (i - avg) ** 2 / float(len(args) - 1)
    return (deviation)

