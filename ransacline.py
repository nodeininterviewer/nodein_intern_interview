import numpy as np
import matplotlib.pyplot as plt
from random import randint

#Generates noisy data points for a line
#Using form y=mx+c
#m=slope
#c=y-intercept
#noise=std deviation for noise threshold
def GenerateLine(m,c,noise,num_off_points):
    distribution=np.random.normal(0,noise,num_off_points)
    x_points=np.linspace(10,200,num_off_points)
    xs=[]
    ys=[]
    for i in range(0,num_off_points):
        xs.append(x_points[i])
        y=m*x_points[i]+c
        y=y+distribution[i]
        ys.append(y)
    return xs,ys

#Generates a line without any noise
def GenerateLineNoNoise(m,c,num_off_points):
    x_points=np.linspace(10,200,num_off_points)
    xs=[]
    ys=[]
    for i in range(0,num_off_points):
        xs.append(x_points[i])
        y=m*x_points[i]+c
        ys.append(y)
    return xs,ys


#Generates the noisy dataset with inliers and outliers
def CreateProblem():
    noise=20
    slope=7
    y_intercept=4
    num_of_points=300
    x,y=GenerateLine(slope,y_intercept,noise,500)

    outlier_x,outlier_y=GenerateLine(12,100,30,100)
    x=x+outlier_x
    y=y+outlier_y
    outlier_x2,outlier_y2=GenerateLine(-3,-80,30,100)
    x=x+outlier_x2
    y=y+outlier_y2
    return x,y

#DO NOT MODIFY ANY CODE ABOVE THISE LINE

#x = x coordinates of the datapoints
#y = y coordinates of the datapoints
def RANSAC(x,y):
    solution_m=0
    solution_c=0
    best_error=10000
    data_size = len(x)
    best_inliners = 0
    thresh = 100
    #for k number of iterations
    k = 0
    while(k<30):
        inliner_error = 0
        num_inliners = 0
        #randomly select two pts from data
        r1 = randint(0,data_size-1)
        r2 = randint(0,data_size-1)
        while r2 == r1: r2 = randint(0,len(x))

        #fit line to pts
        curr_m,curr_c = fitline(x[r1],y[r1],x[r2],y[r2])

        #print(x[r1],x[r2],y[r1],y[r2])
        #for all data points not in curr_inliners
        for i in range(0,2):
            if i!= r1 and i!= r2:
                pt_dist = testfit(x[i],y[i],curr_m,curr_c)
                if pt_dist < thresh:
                    #this point belongs to inliners
                    inliner_error += pt_dist
                    num_inliners += 1
        if(inliner_error < best_error and num_inliners > best_inliners):
            best_error = inliner_error
            solution_m= curr_m
            solution_c= curr_c
        k+=1
    return solution_m,solution_c

#takes in points a and b
#outputs m and c for line equation
def fitline(x1,y1,x2,y2):
    m = (y2-y1)/(x2-x1)
    c = y1-m*x1
    return m,c

#takes in point (x,y) and line parameters
#outputs distance from point to line
def testfit(x,y,m,c):
    d1 = ((x+(m*y)-(m*c))/(m**2 +1))**2
    d2 = (m*(x+(m*y)-(m*c))/(m**2 +1)+c-y)**2
    d  = np.sqrt(d1+d2)
    return d

x,y=CreateProblem()

sol_m,solution_c=RANSAC(x,y)

sol_x,sol_y=GenerateLineNoNoise(sol_m,solution_c,30)

#Plot data and solution
plt.plot(x,y,'ro')
plt.plot(sol_x,sol_y,linewidth=2.0)
plt.show()
