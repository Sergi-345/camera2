


# class Frame():
#     def __init__(self):
#         self.frameList=[]
#         self.side=""
#         self.tsList=[]
#         self.results=[]
#         self.player_list=[]
#         self.ball_list=[]
#         self.racket_list=[]
#         self.kick_init_list=[]
#         self.reception_player_index_list=[]
#         self.reception_quadrant_ball_list=[]
#         self.reception_player_id_list=[]
#         self.kick_side_list=[]
#         self.ballBounceAfterKick_list=[]
        
class Frame():
    def __init__(self):
        self.frame=[]
        self.side=""

        ## LISTS
        self.player_list=[]
        self.ball_list=[]
        self.racket_list=[]
        self.ballBounceAfterKick_list=[]

        self.kick_init=0
        self.reception_player_index=0
        self.reception_quadrant_ball=0
        self.reception_player_id=0
        self.kick_side=0