MAPS = []

def make_maps(tsize):
    global MAPS
    # colision maps with bbox for drawing and making walls
    MAPS.append([[[3    , tsize[1]-4], [tsize[0]-64, tsize[1]]-1],
                 [[14, tsize[1]-8], [17, tsize[1]-5]],
                 [[22, tsize[1]-15], [32, tsize[1]-13]],
                 [[33, tsize[1]-12], [44, tsize[1]-10]],
                 [[45, tsize[1]-11], [53, tsize[1]-9]],
                 [[62, tsize[1]-12], [64, tsize[1]-10]],
                 [[69, tsize[1]-12], [71, tsize[1]-10]]])

make_maps([160,60])
for i in MAPS[0]:
    print(i)