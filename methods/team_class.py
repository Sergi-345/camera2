from collections import deque

class TEAM():
    def __init__(self):
        
        self.frameList_BottomLine=[]
        self.acum1=[]
        self.acum2=[]
        self.acum3=[]
        self.acum4=[]
        self.dist_acum_matrix=[self.acum1,self.acum2,self.acum3,self.acum4]

        self.dist_acum_vect=[0,0,0,0]

        self.coord_vect1=[]
        self.coord_vect2=[]
        self.coord_vect3=[]
        self.coord_vect4=[]

        self.coord_matrix=[self.coord_vect1,self.coord_vect2,self.coord_vect3,self.coord_vect4]

        self.buffer_results_L=deque(maxlen=10)
        self.buffer_results_R=deque(maxlen=10)

    player_list=[]
    racket_list=[]
    ball_list=[]
    frame=[]
    frame2=[]
    frame2_cpu=[]
    frame_final=[]
    x_acum=[]
    y_acum=[]
    background=[]
    newSubstractor=[]
    bck=[]
    local_model=[]
    results=[]
    frameList=[]
    results_support=[]
    results_shoes=[]
    local_model_support=[]
    local_model_shoes=[]
    nPlayers=0
    init=0
    kick_position_count=0
    kick_init=0
    afterKick_init=0
    kick_finished=0
    afterKick_duration_counter=0
    ballBounceAfterKick_list=[]
    curr_player_net_index=0
    kick_side=0
    reception_side=0
    reception_height=0
    reception_quadrant_player=50
    reception_quadrant_ball=50
    initial_id=0

    curr_player_kick_index=50
    curr_player_kick_id=50

    reception_player_id=50
    reception_player_index=50

    reception_player_vel=0
    kick_player_vel=0
    net_player_vel=0

    n_kicks=[0,0,0,0]
    kicks_order=[]
    counter_kicks=0

    vel_vect=[]
    kick_vect=[]

    ball_bounce_init=0
    ball_bounce_counter=0
    ball_noDet_counter=0
    ball_bounce_list = []
    prev_ball_list=[]
    ball_list_fullRange=[]

    th_overlaping = 20
    count_frames_no_bounce=0

    point_playing=0
    counter_change_players=0

    player_missing_vector=[0,0,0,0]
    change_side=0
    change_side_count=0
    player_height=[[0,0],[0,0]]
    player_prev_height=[[0,0],[0,0]]

    counter_in_defense=[0,0,0,0] # Player ID 1,2,3,4
    counter_in_transition=[0,0,0,0] # Player ID 1,2,3,4
    counter_in_attack=[0,0,0,0] # Player ID 1,2,3,4

    match_line1=[[0,0],[0,0]]
    match_line2=[[0,0],[0,0]]
    match_line3=[[0,0],[0,0]]
    match_line4=[[0,0],[0,0]]
    missing=[0,0]

    new_serve_allowed=1
    quadrant_change_during_ball_bounce=0

    q_pos=[[1,3],[2,4]]

    frameSupport_BottomLine=[]

    ball_detected_background_list=[]

    partners_vector=[3,4,1,2]

    serve_player_id=1
    net_player_id=1

    serve_team_sequence_vector=[]
    last_team_serve=0
    next_team_serve=0
    last_serve_ball=0  
    serve_change=0  

    ball_top_counter = 0

    ball_in_top_list=[]

    trackers=[]

