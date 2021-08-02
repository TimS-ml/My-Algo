def rotateImage(a):
    a[:] = zip(*a[::-1])
    return a
