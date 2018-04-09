import matplotlib.pyplot as plt
import sympy as sp
import numpy as np
from numpy import *
from sympy import *
import os, glob, time


def latexSeries(formula, indipendent_variable, N, x0=0):
    formula = sympify(formula)
    indipendent_variable = symbols(indipendent_variable)
    latex = sp.latex(formula.series(indipendent_variable, x0, N+1))
    print(latex)
    return latex


# change formula to series expansion
def formula2series(formula, indipendent_variable, N, xMin, xMax, yMin, yMax, c, d, x0=0):
    # translate to sympy

    formula = sympify(formula)
    indipendent_variable = symbols(indipendent_variable)
    # make into series equation now
    formulaSeries = formula.series(indipendent_variable, x0, N + 1).removeO()
    formulaSeries = sp.lambdify(indipendent_variable, formulaSeries, modules=['numpy'])
    t = np.linspace(xMin, xMax)
    # plot the series expansion formula
    form_fun = sp.lambdify(indipendent_variable, formula)
    if c == 'yes' or c == 'Yes':

        fig, ax = plt.subplots()
        ax.set_xlim((xMin, xMax))
        ax.set_ylim((yMin, yMax))
        ax.plot(t, formulaSeries(t), t, form_fun(t))
        ax.set(xlabel='X Axis ', ylabel='Y Axis',
               title='Exercise Four Graph')
        if d == 'top right' or d == 'Top Right':
            ax.legend(loc=1)
        elif d == 'bottom right' or d == 'Bottom Right':
            ax.legend(loc=4)
        elif d == 'bottom left' or d == 'Bottom Left':
            ax.legend(loc=3)
        elif d == 'top left' or d == 'Top Left':
            ax.legend(loc=2)
        ax.grid()
        fig.savefig("test.png")
    elif c == 'no' or c == 'No':
        Nstr = str(N)
        plt.ylim(yMin, yMax)
        plt.plot(t, formulaSeries(t), label=('Series, N = ', Nstr))
        plt.title("Exercise Four Graph")
        if d == 'top right' or d == 'Top Right':
            plt.legend(loc=1)
        elif d == 'bottom right' or d == 'Bottom Right':
            plt.legend(loc=4)
        elif d == 'bottom left' or d == 'Bottom Left':
            plt.legend(loc=3)
        elif d == 'top left' or d == 'Top Left':
            plt.legend(loc=2)








def compute(formula, indipendent_variable, N, xMin, xMax, yMin, yMax, eCurves, legLoc):
    # print(type(formula))
    # print(type(indipendent_variable))
    # print(type(N))
    # print(type(xMin))
    # print(type(xMax))
    # print(type(yMin))
    # print(type(yMax))
    # print(type(x0))
    formula2series(formula, indipendent_variable, N, xMin, xMax, yMin, yMax, eCurves, legLoc)
    if not os.path.isdir('static'):
        os.mkdir('static')
    else:
        # Remove old plot files
        for filename in glob.glob(os.path.join('static', '*.png')):
            os.remove(filename)
        # Use time since Jan 1, 1970 in filename in order make
        # a unique filename that the browser has not chached
    plotfile = os.path.join('static', str(time.time()) + '.png')
    plt.savefig(plotfile)
    return plotfile


if __name__ == '__main__':
    # compute(formula, IV, N, xmin, xmax, ymin, ymax, 0)
    compute('exp(-2*t)', 't', 3, 0, 2, -6, 1, 0)
    latexSeries('sin(x)', 'x', 12, 0)
