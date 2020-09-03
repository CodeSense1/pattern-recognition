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

def onclick(evt):
    # print(f"button ({evt.button}), x=({evt.x}), y=({evt.y}), xdata=({evt.xdata}), ydata=({evt.ydata})")
    
    # Left mouse button
    if evt.button == 1 and evt.xdata is not None and evt.ydata is not None:
        
        plotPoints(evt.xdata, evt.ydata)
        drawline(x,y)        
    
    # Right mouse button
    elif evt.button == 3:
        plt.close(fig)

        
        

def plotPoints(xdata,ydata):
    # add new point and draw all previously added points
    x.append(xdata)
    y.append(ydata)
    plt.plot(xdata, ydata, 'kx')
    fig.canvas.draw()

def drawline(x,y):

    if len(x) < 2 or len(y) < 2:
        return

    
    a,b = linregress(x,y)
    
    print("My fit: a = {:.4f} and b = {:.4f}".format(a,b))

    xp = np.arange(0, 10,0.1)
    
    regression.set_data(xp, a*xp + b)

    aText.set_text("a = {:.4f}".format(a))
    bText.set_text("b = {:.4f}".format(b))

    fig.canvas.draw()
    fig.canvas.flush_events()
    plt.legend(["Regression", "points"])


def init():
    fig = plt.figure(figsize=(8,8))
    ax = fig.add_subplot(111)
    ax.set_xlim([0, 10])
    ax.set_ylim([0, 10])


    dx = np.arange(0, 10,0.1)
    dy = dx
    regLine, = plt.plot(dx, dy,'r-')
    regLine.set_figure(fig)

    aText = plt.text(0.5,8, "a = 1")
    bText = plt.text(0.5,7.7, "b = -2") 

    plt.legend(["Regression"])

    fig.canvas.mpl_connect('button_press_event', onclick)
    return fig, ax, regLine, aText, bText



# Define x,y points
x = []
y = []

fig, ax, regression, aText, bText = init()
plt.show()

