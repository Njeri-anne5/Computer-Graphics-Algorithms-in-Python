# Line Drawing Algorithms


## Algorithm 1
### [Cartesian Slope Intercept Equation](https://www.javatpoint.com/computer-graphics-scan-converting-a-straight-line)

Cartesian Slope Intercept Equation

y = m*x + b \
m = (y2 - y1) / (x2 - x1) \
b = y1 - m * x1 \
▲y = m * ▲x \


## Algorithm 2
### [DDA ( digital diffrential analyzer ) Algorithm](https://www.javatpoint.com/computer-graphics-dda-algorithm)

This algorithm is summarized in the following procedure, which accepts as input the two endpoint pixel positions. Horizontal and vertical differences between the endpoint positions are assigned to parameters dx and dy. The difference with the greater magnitude determines the value of parameter steps. Starting with pixel position (xa, ya), we determine the offset needed at each step to generate the next pixel position along the line path. We loop through this process steps times. If the magnitude of dx is greater than the magnitude of dy and xa is less than xb, the values of the increments in the x and y directions are 1 and m,
respectively. If the greater change is in the x direction, but xa is greater than xb, then the decrements - 1 and -m are used to generate each new point on the line. Otherwise, we use a unit increment (or decrement) in they direction and an x increment (or decrement) of l/m. 


## Algorithm 3
### [Bresenham's Line Algorithm](https://www.javatpoint.com/computer-graphics-bresenhams-line-algorithm)