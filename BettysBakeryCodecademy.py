import numpy as np

cupcakes = np.array([2, 0.75, 2, 1, 0.5])
recipes = np.array([[1.00,  0.125,    1,  1,  0.125],
                   [2.75,  1.500,    1,  0,  1.000],
                   [4.00,  0.500,    2,  2,  0.500]])

eggs = recipes[:, 2]
print(eggs)
one_egg = recipes[(eggs == 1)]
print(one_egg)

cupcakes = recipes[0, :]
cookies = recipes[2, :]

double_batch = 2 * cupcakes
grocery_list = cookies + double_batch
print(grocery_list)
