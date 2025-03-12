

def cut_frame(frame,MainWindow,actual_height,actual_width):
    cut_width=MainWindow.params["cut_width"]
    cut_height=MainWindow.params["cut_height"]
    y0=0
    x0=0
    xEnd=int(actual_width)
    yEnd=int(actual_height)

    if cut_height < actual_height:
        y0 = int(actual_height-cut_height)
    if cut_width < actual_width:
        x0= int((actual_width-cut_width)/2)
        xEnd = int(actual_width-int((actual_width-cut_width)/2) )
    

    frame = frame[y0:yEnd,x0:xEnd]  # Correct slicing order
    return frame