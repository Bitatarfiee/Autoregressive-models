# Autoregressive-models
Autoregressive models

# Dependencies
pandas 
numpy 
matplotlib.pyplot
sklearn import linear_model #Used for solving linear regression problems
from sklearn.neural_network import MLPRegressor #Used for NAR model
from tssltools_lab1 import acf, acfplot #Used for plotting ACF
from sklearn.metrics import mean_squared_error


# files and descriptions
Dataset: sealevel.csv , The data is taken from https://climate.nasa.gov/vital-signs/sea-level/ 

Model: autoregressive_model.py

one-step-ahead prediction of AR model 

ACF model and plot: Computes the empirical autocorralation function and Plots the empirical autocorralation function.

Long-range predictions: Simulates an AR(p) model for m steps, with initial condition given by the last p values of y

Nonlinear AR model:  a nonlinear autoregressive (NAR) model, which is based on a feedforward neural network. 