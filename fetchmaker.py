import os
import numpy as np
import pandas as pd
os.chdir('C:/Users/Adrian/Documents/Data Journalism/Datacamp Lesson'
         'Datafiles/')
rottweiler_tl = pd.read_csv('rottweiler_tl.csv', delimiter="  ", header=None)
print(rottweiler_tl.mean())
print(rottweiler_tl.std())
