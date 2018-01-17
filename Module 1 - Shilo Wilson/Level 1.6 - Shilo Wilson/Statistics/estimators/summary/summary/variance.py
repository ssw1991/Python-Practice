from estimators.summary.summary.mean import mean as mean


def variance(container, degOfFreedom=1):
    """
    Returns Variance of passed in list

    """
    avg = mean(container)
    deviation = 0

    for i in container:
        deviation += (i - avg) ** 2 / float(len(container) - degOfFreedom)
    return (deviation)