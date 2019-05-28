# server.py
from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer
from model import MoneyModel
from mesa.visualization.modules import ChartModule
from mesa.visualization.UserParam import UserSettableParameter


CELLS = 30


def agent_portrayal(agent):
    portrayal = {"Shape": "circle",
                 "Color": "red",
                 "Filled": "true",
                 "Layer": 0,
                 "r": 0.8}
    if agent.wealth > 0:
        portrayal["Color"] = "red"
        portrayal["Layer"] = 0
    else:
        portrayal["Color"] = "grey"
        portrayal["Layer"] = 1
        portrayal["r"] = 0.4
    return portrayal


grid = CanvasGrid(agent_portrayal, CELLS, CELLS, 300, 300)

chart = ChartModule([{"Label": "Gini",
                      "Color": "Black"}],
                    data_collector_name='datacollector')

n_slider = UserSettableParameter('slider', "Number of Agents", 100, 2, 1000, 1)

server = ModularServer(MoneyModel,
                       [grid, chart],
                       "Money Model",
                       {"N": n_slider, "width": CELLS, "height": CELLS})

