import matplotlib.pyplot as plt
import numpy as np
import uuid
import sys
import matplotlib
matplotlib.use('Agg')


def generate_asset_code(value):
    """This function create the Unique ID for the Asset Type"""
    foo = [x for x in value if x != '.']
    bar = "".join(foo)

    return bar[-1:-17:-1]


def pie_chart():
    y = np.array([35, 25, 25, 15])
    mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

    plt.pie(y, labels=mylabels, startangle=90)
    plt.show()

    # Two  lines to make our compiler able to draw:
    result1,result2 = plt.savefig(sys.stdout.buffer),sys.stdout.flush()

    return plt.show()
