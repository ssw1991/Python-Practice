import summary.summary_func


def output(values, pop = True):
    """
    prints output to console
    :param values:
    :param pop:
    :return:  NONE
    """

    if pop:
        vals = summary.summary_func.summary_pop(values)
        print 'Mean is {}'.format(vals[0])
        print 'Variance is {}'.format(vals[1])

    else:
        vals = summary.summary_func.summary_sample(values)
        print 'Mean is {}'.format(vals[0])
        print 'Variance is {}'.format(vals[1])
