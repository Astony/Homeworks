def custom_range(collection, *args, step=1):
    if len(args) == 3:
        start, stop, step = args
        return collection[collection.index(start) : collection.index(stop) : step]
    elif len(args) == 1:
        stop = args[0]
        start = collection[0]
        if step < 0:
            start, stop = stop, start
            return collection[collection.index(start) : collection.index(stop) : step]
        return collection[collection.index(start) : collection.index(stop) : step]
    start, stop = args
    return collection[collection.index(start) : collection.index(stop) : step]
