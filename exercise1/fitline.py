import matplotlib.pyplot as plt
import scipy.stats as sp
import numpy as np

def linregress(xd,yd):
    # Define values for linear regression
    xmean = sum(xd)/len(xd)
    ymean = sum(yd)/len(yd)

    num = 0
    den = 0
    for x,y in zip(xd, yd):
        num += (x-xmean)*(y-ymean)
        den += (x-xmean) * (x-xmean)

    a = float(num)/float(den)
    b = ymean - a*xmean
    
    return a,b

# Define x,y points
x = []
y = []

def onclick(evt):
    print(f"button ({evt.button}), x=({evt.x}), y=({evt.y}), xdata=({evt.xdata}), ydata=({evt.ydata})")
    
    # Left mouse button
    if evt.button == 1 and evt.xdata is not None and evt.ydata is not None:
        fig.clear()
        ax.set_xlim([-2, 5])
        ax.set_ylim([-2, 5])
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

    if len(x) < 2 or len(y) < 2:
        print("x or y has too few values!")
        return

    a,b = linregress(x,y)
    
    print(f"My fit: a = {a} and b = {b}")

    xp = np.arange(-2,5,0.1)
    plt.plot(xp, a*xp + b, 'r-')
    plt.legend(["points", "Regression"])


def init():
    fig = plt.figure(figsize=(8,8))
    ax = fig.add_subplot(111)
    ax.set_xlim([-2, 5])
    ax.set_ylim([-2, 5])
    fig.canvas.mpl_connect('button_press_event', onclick)
    return fig, ax


fig, ax = init()
plt.show()
