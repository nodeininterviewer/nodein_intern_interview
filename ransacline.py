import numpy as np
import matplotlib.pyplot as plt

#Using form y=mx+c
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

def GenerateLineNoNoise(m,c,num_off_points):
    x_points=np.linspace(10,200,num_off_points)
    xs=[]
    ys=[]
    for i in range(0,num_off_points):
        xs.append(x_points[i])
        y=m*x_points[i]+c
        ys.append(y)
    return xs,ys

def CreateProblem():
    noise=20
    slope=7
    y_intercept=4
    num_of_points=300
    x,y=GenerateLine(slope,y_intercept,noise,500)

    outlier_x,outlier_y=GenerateLine(12,100,30,20)
    x=x+outlier_x
    y=y+outlier_y
    outlier_x2,outlier_y2=GenerateLine(-3,-80,30,20)
    x=x+outlier_x2
    y=y+outlier_y2
    return x,y

#DO NOT MODIFY ANY CODE ABOVE THISE LINE


def RANSAC(x,y):
    solution_m=0
    solution_c=0

    ##Your RANSAC solution here

    return solution_m,solution_c

x,y=CreateProblem()

sol_m,solution_c=RANSAC(x,y)

sol_x,sol_y=GenerateLineNoNoise(sol_m,solution_c,30)

#Plot data and solution
plt.plot(x,y,'ro')
plt.plot(sol_x,sol_y,linewidth=2.0)
plt.show()