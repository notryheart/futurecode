for x in range(0,2):
    for y in range(0,2):
        for z in range(0,2):
            for w in range(0,2):
                f = (not(y <= x)) or ((not z) <= (not w)) or z
                if f == 0:
                    print(z,y,w,x)