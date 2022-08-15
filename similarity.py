def similarity(linea, lineb):
    r""" The Levenshtein distance is a text similarity measure
         that compares two words and returns a numeric value
         representing the distance between them. The distance
         reflects the total number of single-character edits
         required to transform one word into another.
         The more similar the two words are the less distance
         between them, and vice versa.

    This is a recursive module calculating the similarity
    of two strings ( Levenshtein distance ).

    return - minimum number of single-character edits
             (insertions, deletions or substitutions)
             required to change one line into the other

    >>> similarity("Qwertyuiop","Qwertyuiop")
    0
    >>> similarity("Q1ertyuiop","Q2ertyuiop")
    1
    >>> similarity("12-Qwertyuiop","Qwertyuiop")
    3
    """
    assert len(linea) > 0, "It's a bad length"
    return _similarity(linea, lineb)


def _similarity(linea, lineb, i=0, j=0, results=None):
    if results == None:
        results = {}

    if not len(linea[i:]) or not len(lineb[j:]):
        return len(linea[i:]) + len(lineb[j:])

    res_ab = results.get((i, j))
    if res_ab:
        return res_ab

    res_a1b1 = _similarity(linea, lineb, i + 1, j + 1, results)
    if linea[i] == lineb[j]:
        results.update({(i, j): res_a1b1})
        if i == j == 0:
            res_print(linea, lineb, results)
        return res_a1b1
    else:
        res_ab1 = _similarity(linea, lineb, i, j + 1, results)
        res_a1b = _similarity(linea, lineb, i + 1, j, results)
        res_ab = min(res_a1b1, res_ab1, res_a1b) + 1
        results.update({(i, j): res_ab})
        if i == j == 0:
            res_print(linea, lineb, results)
        return res_ab


def res_print(a, b, results):
    for i in range(len(a)):
        s = ""
        for j in range(len(b)):
            r = results.get((i, j))
            s += "  {0}".format(r) if r else "  -"
        print(s)


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    print(similarity("Qwerty23", "Qwertyui1p23"))
