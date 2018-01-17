from summary.mean import mean as mean
from summary.variance import variance as variance

def summary_pop(values):
    """
    computes the variance and mean of a container, returns tuple (mean, variance)
    :param values: containter
    :return: tuple (mean, variance)
    """

    return (mean(values), variance(values, degOfFreedom =0))


def summary_sample(values):
    """
    computes the variance and mean of a container, returns tuple (mean, variance)
    :param values: containter
    :return: tuple (mean, variance)
    """

    return (mean(values), variance(values))



