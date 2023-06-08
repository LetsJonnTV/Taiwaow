from settings import *



from dp.taiwaow_dp import *
if Taiwaow_dp_v2_ac == True:
    Taiwaow_dp_v2 = Taiwaow_dp(taiwaow_tkinter, taiwaow_math, taiwaow_fastapi, taiwaow_os, taiwaow_sys, taiwaow_torch, taiwaow_tensorboard, taiwaow_numpy, taiwaow_pandas, taiwaow_matplotlib, taiwaow_seaborn)


from fe.taiwaow_fe import *
if Taiwaow_dp_v2_ac == True:
    Taiwaow_fe_v2 = Taiwaow_fe(ti,pg,tki)
    

from be.taiwaow_be import *
if Taiwaow_fe_v2_ac == True:
    Taiwaow_be_v2 = Taiwaow_be(requests, o,s)