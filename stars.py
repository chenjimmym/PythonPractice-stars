def draw_stars(arr):
    for data in arr:
        if isinstance(data, int):
            print '*'*data
        if isinstance(data, str):
            print data[0].lower()*len(data)



x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
draw_stars(x)