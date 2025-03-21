import cv2

def draw_racket(cFrame):
    cnt=-1
    for result in cFrame.results:
        cnt+=1
        for racket in cFrame.racket_list[cnt]:           
            cv2.rectangle(result.orig_img, (racket.pos.x0, racket.pos.y0), (racket.pos.xEnd, racket.pos.yEnd), (0, 0, 255), 2)
        