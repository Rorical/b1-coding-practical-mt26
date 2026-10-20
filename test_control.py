from uuv_mission.control import PDController

c = PDController()
print(c.compute(1.0, 0.0))  # 0.15*1 + 0.6*(1-0)   = 0.75               -> expected output: 0.75
print(c.compute(1.0, 0.5))  # 0.15*0.5 + 0.6*(0.5-1) = -0.225           -> expected output: -0.225