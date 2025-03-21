from methods import pos_class


class RACKET():
    def __init__(self,id):

        self.id=id
        self.pos=pos_class.POS()
    id=0
    pos=[]
    x0=0
    xEnd=0
    y0=0
    yEnd=0
    frame=[]
    conf=0
    side=0