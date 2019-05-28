# run.py
from model import *
import numpy as np
import matplotlib.pyplot as plt

model = MoneyModel(10000, 50, 50)
for i in range(20):
    model.step()

agent_counts = np.zeros((model.grid.width, model.grid.height))
for cell in model.grid.coord_iter():
    cell_content, x, y = cell
    agent_count = len(cell_content)
    agent_counts[x][y] = agent_count

plt.figure(figsize=(4, 3))
plt.imshow(agent_counts, interpolation='nearest')
plt.colorbar()

gini = model.datacollector.get_model_vars_dataframe()
gini.plot(figsize=(4, 3))
plt.show()
