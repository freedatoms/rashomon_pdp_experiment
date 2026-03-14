import numpy as np

def gt_scenario_1(X1,X2,X3,X4,X5,X6,X7,X8,X9):
    return 2.9*X1 - 3.7*X2+1.2*X3+0.8*X1*X1-1.5*X2*X3+1.1*X4-0.5*np.log(X5+1) + \
           np.where(X6 == "B", 2, np.where(X6=="C", -1, 0)) + 0.3*X9

def gt_scenario_2(X1,X2,X3,X4,X5,X6,X7,X8,X9):
    return np.sin(X1) + np.log(np.abs(X3)+1)+0.8*X4*X5 - 1.2*X1*X3 + np.where(X6 == "A", -2, np.where(X6=="C", 1, 0)) + \
         1.5*X7+np.where(X8 == "1", 2, 0) + 0.4*X9*X9

def gt_scenario_3(X1,X2,X3,X4,X5,X6,X7,X8,X9):
    def f(x):
        return 0.08*np.where(x>=0, 0.5*np.tanh(x)+0.1*np.sqrt(np.abs(x)), -np.sqrt(np.abs(2*x))) + 0.85
    return f(X1) + 2*X2+0.5*np.exp(-(X3*X3))+0.7*np.sin(np.pi*X4)+0.6*X5**0.3+np.where(X6=='C',3,0)+\
         0.9*X7+1.2*X9