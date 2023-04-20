def word_search(doc_list, keyword):
    """
    Takes a list of documents (each document is a string) and a keyword.
    Returns list of the index values into the original list for all documents
    containing the keyword.

    Example:
    >>> doc_list = ["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"]
    >>> word_search(doc_list, 'casino')
    [0]

    """
    index_list = []
    key = keyword.lower()
    for i in doc_list:
        a = doc_list.index(i)
        for word in i.lower().replace('.','').replace(',','').split(" "):
            if key ==word:
                if a not in index_list:
                    index_list.append(a)
    return index_list