from collections import Counter
#sort elements by the most common to least common

def most_common(elements):
    elements = Counter(elements).most_common()
    #return elements
    values = []
    for value in elements:
       values.append(value[0])
    return values

