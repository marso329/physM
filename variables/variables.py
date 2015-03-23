objects_in_world={}
number_of_objects_in_world=0
window=None
background_color=(0,0,0,0)
background_color_string="BLACK"
viewing_center=(0,0,0)
viewing_position=(0,-22,0)
key_bindings={}


#for fps counting
timer_resolution=0.1
fps_timer=timer_resolution
fps=False
fps_time=0.0
fps_counter=0.0
current_fps=0.0

#for holding a fps
holding_fps=30
holding_timer=timer_resolution
holding_change_time=0
holding_sleep=0.0
holding_delta=2.0
holding=False
functions_in_mainloop=0
functions_to_run_in_mainloop={}

gravity_vector=(0,0,-2.82)

distance_for_collision=0.01