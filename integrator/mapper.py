"""
The map function maps several inputs
to the same number of outputs using the function fx provided.
"""

def map(fx, inp):
    results=[]
    for x in inp:
        results.append(fx.cal(x))

    return results
