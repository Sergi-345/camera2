import cv2

def draw_matches(perm_team, frame):
    pt1 = (int(perm_team.match_line1[0][0]), int(perm_team.match_line1[0][1]))
    pt2 = (int(perm_team.match_line1[1][0]), int(perm_team.match_line1[1][1]))

    cv2.line(frame, pt1, pt2, [0,255,0], thickness=4)

    pt1 = (int(perm_team.match_line2[0][0]), int(perm_team.match_line2[0][1]))
    pt2 = (int(perm_team.match_line2[1][0]), int(perm_team.match_line2[1][1]))

    cv2.line(frame, pt1, pt2, [0,0,255], thickness=4)

