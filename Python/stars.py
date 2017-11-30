x= [4,6,1,3,5,7,25,"blaine"]
def draw_stars(arr):
    for placeInArray in x:
        if type(placeInArray) is int:
            a = ""
            for index in range(0, placeInArray):
                a += "*"
            print (a)
        elif type(placeInArray) is str:
            count = 0
            lstr =""
            for index in range(0, len(placeInArray)):
                count += 1
                lstr += placeInArray[:1]
            print (lstr)
draw_stars(x)