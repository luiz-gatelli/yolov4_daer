import PySimpleGUI as sg
import numpy as np
from matplotlib.widgets import RectangleSelector
import matplotlib.figure as figure
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import json
import pandas as pd
import sklearn as sk

# Image general definitions
HEIGHT = 1080
WIDTH = 1920
data_file = 'data_tresh03.txt'
data = pd.read_json(data_file, 'records').T

data["x_initial"] = (data["initial position"].str[0] +
                     data["initial position"].str[2]) / 2
data["x_final"] = (data["last position"].str[0] +
                   data["last position"].str[2]) / 2
data["y_initial"] = -(data["initial position"].str[1] +
                      data["initial position"].str[3]) / 2 + HEIGHT
data["y_final"] = -(data["last position"].str[1] +
                    data["last position"].str[3]) / 2 + HEIGHT

data.to_csv("exemplo.csv")

# Matplotlib Figure - Initialize
fig = figure.Figure()
ax = fig.add_subplot(111)
ax.axis('off')
px = 1/fig.get_dpi()
fig.set_size_inches(WIDTH*px, HEIGHT*px)


def draw_figure(canvas, fig):
    if canvas.children:
        for child in canvas.winfo_children():
            child.destroy()
    figure_canvas_agg = FigureCanvasTkAgg(fig, master=canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='right', fill='both', expand=1)


layout = [
    [sg.Checkbox("Car", default=False, key='car', enable_events=True), sg.Checkbox("Truck", default=False, key='truck', enable_events=True),
     sg.Checkbox("Motorcycle", default=False, key='motorcycle', enable_events=True), sg.Checkbox("Bus", default=False, key='bus', enable_events=True)],
    [sg.Canvas(key='fig_canvas', size=(WIDTH*px, HEIGHT*px))]
]

window = sg.Window('Visualizer', layout, size=(
    WIDTH * 8 // 10, HEIGHT * 8 // 10))
window.read()


def plot_arrow(ax, data, color):
    ax.scatter(data["x_initial"].values, data["y_initial"].values,
               c='blue', marker='o', s=10, zorder=3)
    ax.scatter(data["x_final"].values,
               data["y_final"].values, c='red', marker='o', s=10, zorder=2)

    ax.quiver(data["x_initial"].values, data["y_initial"].values, ((data["x_final"] - data["x_initial"]).values),
              ((data["y_final"] - data["y_initial"]).values), angles="xy", scale_units="xy", scale=1, width=0.002, color=color)


ax.scatter(data["x_initial"].values, data["y_initial"].values,
           c='blue', marker='o', s=10, zorder=3)
ax.scatter(data["x_final"].values,
           data["y_final"].values, c='red', marker='o', s=10, zorder=2)


draw_figure(window['fig_canvas'].TKCanvas, fig)

while True:
    event, values = window.read()
    # elif values['car'] == True:
    if event == sg.WIN_CLOSED or event == "Exit":
        break
    ax.clear()
    ax.axis('off')
    if values['car'] == True:
        plot_arrow(ax, data.loc[data['class'] == 'car'], 'black')
    if values['motorcycle'] == True:
        plot_arrow(ax, data.loc[data['class'] == 'motorcycle'], 'green')
    if values['bus'] == True:
        plot_arrow(ax, data.loc[data['class'] == 'bus'], 'orange')
    if values['truck'] == True:
        plot_arrow(ax, data.loc[data['class'] == 'truck'], 'purple')

    # ax.quiver([data["x_initial"].values, data["y_initial"].values], [
    #              data["x_final"].values, data["y_final"].values])
    draw_figure(window['fig_canvas'].TKCanvas, fig)

window.close()
