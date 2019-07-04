import numpy as np

calorie_stats = np.array([70,  120,  70,   50,  110,  110,  110,  130,   90,
                         90,
                         120,  110, 120,  110,  110,  110,  100,  110,  110,
                         110,
                         100, 110,  100,  100, 110,  110,  100,  120,  120,
                         110,  100,
                         110,  100,  110,  120,  120, 110,  110,  110,  140,
                         110,
                         100,  110,  100,  150,  150,  160,  100, 120,  140,
                         90,
                         130,  120,  100,   50,   50,  100,  100,  120,  100,
                         90,  110, 110,   80,   90,   90,  110,  110,   90,
                         110,  140,
                         100,
                         110,  110,  100,  100,  110])

calorie_average = np.mean(calorie_stats)
print(calorie_average)
calorie_stats_sorted = np.sort(calorie_stats)
print(calorie_stats_sorted)
percent_greater = np.mean(calorie_stats > 60)
print(percent_greater)
calorie_std = np.std(calorie_stats)
print(calorie_std)
