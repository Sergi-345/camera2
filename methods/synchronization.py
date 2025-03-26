from collections import deque
import queue as q
import cv2

class buffer_data:

    cFrame_listL = deque(maxlen=1000)
    cFrame_listR = deque(maxlen=1000)

    def add_data(self,cFrame_list):
        cnt=-1
        for cFrame in cFrame_list:
            cnt+=1
            if cFrame.side== "L":
                self.cFrame_listL.append(cFrame)
            if cFrame.side== "R":
                self.cFrame_listR.append(cFrame)


    def data_Extraction(self):
        min_size=10
        cFrame_List=[]
        if len(self.cFrame_listL)>min_size and len(self.cFrame_listR)>min_size:
            cFrame_List.append(self.cFrame_listL.popleft())
            cFrame_List.append(self.cFrame_listR.popleft())
        else:
            cFrame_List=None

        return cFrame_List