def concat_words(*args, separator="."):
    print(separator.join(args))


concat_words("a", "b", "c", "d", separator="_")
