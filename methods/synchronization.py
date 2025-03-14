from collections import deque
import queue as q

class buffer_data:
    ts_L = deque(maxlen=100)
    ts_R = deque(maxlen=100)
    resultsL = deque(maxlen=100)
    resultsR = deque(maxlen=100)

    def add_data(self,cFrame):
        cnt=-1
        for result in cFrame.results:
            cnt+=1
            if cFrame.side== "L":
                self.resultsL.append(result)
            if cFrame.side== "R":
                self.resultsR.append(result)


    def data_Extraction(self):
        min_size=10
        results=[]
        if len(self.resultsL)>min_size and len(self.resultsR)>min_size:
            results.append(self.resultsL.popleft())
            results.append(self.resultsR.popleft())
        else:
            results=None

        return results