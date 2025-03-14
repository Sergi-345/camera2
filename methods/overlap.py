

def rectangle_area(x1, y1, x2, y2):
    """Calculate the area of a rectangle given its coordinates."""
    return abs(x2 - x1) * abs(y2 - y1)

def overlap_area(rect1, rect2):
    """Calculate the overlap area between two rectangles."""
    # Unpack the rectangle coordinates (bottom-left and top-right)
    x1_min, y1_min, x1_max, y1_max = rect1
    x2_min, y2_min, x2_max, y2_max = rect2
    
    # Calculate the coordinates of the intersection rectangle
    x_overlap_min = max(x1_min, x2_min)
    y_overlap_min = max(y1_min, y2_min)
    x_overlap_max = min(x1_max, x2_max)
    y_overlap_max = min(y1_max, y2_max)
    
    # Check if there is an overlap
    if x_overlap_min < x_overlap_max and y_overlap_min < y_overlap_max:
        return rectangle_area(x_overlap_min, y_overlap_min, x_overlap_max, y_overlap_max)
    else:
        return 0  # No overlap

def overlap_percentage(ball1, ball2):

    x0_ball1 = ball1.pos.x0
    y0_ball1 = ball1.pos.y0
    xEnd_ball1 = ball1.pos.xEnd
    yEnd_ball1 = ball1.pos.yEnd
    rect1=[x0_ball1,y0_ball1,xEnd_ball1,yEnd_ball1]

    x0_ball2 = ball2.pos.x0
    y0_ball2 = ball2.pos.y0
    xEnd_ball2 = ball2.pos.xEnd
    yEnd_ball2 = ball2.pos.yEnd
    rect2=[x0_ball2,y0_ball2,xEnd_ball2,yEnd_ball2]

    """Calculate the percentage of overlap between two rectangles."""
    # Calculate areas
    area1 = rectangle_area(*rect1)
    area2 = rectangle_area(*rect2)
    intersection_area = overlap_area(rect1, rect2)
    
    # Overlap percentage can be relative to either rectangle or both
    # Here, we calculate relative to the first rectangle
    return (intersection_area / area1) * 100 if area1 > 0 else 0

def check_overlap(rect1,rect2):
    rect1 = (2, 2, 6, 6)
    rect2 = (4, 4, 8, 8)

    # Calculate percentage of overlap
    percentage_overlap = overlap_percentage(rect1, rect2)