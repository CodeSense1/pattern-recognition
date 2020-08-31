import matplotlib.pyplot as plt
import scipy.stats as sp
import numpy as np

def linregress(xd,yd):
    # Define values for linear regression
    x = np.array(xd)
    y = np.array(yd)
    a = (sum(x*y) - sum(y)/len(y)*sum(x)) / ((sum(x*x) + sum(x)/len(x) * sum(x)))
    b = a*sum(x)/len(x) + sum(y) / len(y)
    return a,b

# Define x,y points
x = []
y = []

def onclick(evt):
    print(f"button ({evt.button}), x=({evt.x}), y=({evt.y}), xdata=({evt.xdata}), ydata=({evt.ydata})")
    
    # Left mouse button
    if evt.button == 1:
        fig.clear()
        plotPoints(evt.xdata, evt.ydata)        
    
    # Right mouse button
    elif evt.button == 3:
        plt.close()
        

def plotPoints(xdata,ydata):
    # add new point and draw all previously added points
    x.append(xdata)
    y.append(ydata)
    plt.plot(x, y, 'kx')
    drawline(x,y)
    fig.canvas.draw()

def drawline(x,y):

    if len(x) < 1 or len(y) < 1:
        print("x or y has too few values!")
        return

    a,b = linregress(x,y)
    t = sp.linregress(x,y)
    a1 = t[0]
    b2 = t[1]

    print(f"My fit: a = {a} and b = {b}")
    print(f"Real regression: a = {a1} and b = {b2}")

    xp = np.arange(-2,5,0.1)
    plt.plot(xp, a*xp + b, 'r-')
    plt.plot(xp, a1*xp + b2, 'g-')
    plt.legend(["points", "My regression", "Scipy regression"])


def init():
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_xlim([-2, 5])
    ax.set_ylim([-2, 5])
    fig.canvas.mpl_connect('button_press_event', onclick)
    return fig


fig = init()
plt.show()
