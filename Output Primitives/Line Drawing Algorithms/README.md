# Line Drawing Algorithms

These algorithms can be used to create straight lines faster. The code for each algorithms is available written in python.

## Algorithm 1
### [Cartesian Slope Intercept Equation](https://www.javatpoint.com/computer-graphics-scan-converting-a-straight-line)

Cartesian Slope Intercept Equation

`y = m*x + b
m = (y2 - y1) / (x2 - x1)
b = y1 - m * x1
▲y = m * ▲x
`

## Algorithm 2
### [DDA ( digital diffrential analyzer ) Algorithm](https://www.javatpoint.com/computer-graphics-dda-algorithm)

This algorithm is summarized in the following procedure, which accepts as input the two endpoint pixel positions. Horizontal and vertical differences between the endpoint positions are assigned to parameters dx and dy. The difference with the greater magnitude determines the value of parameter steps. Starting with pixel position (xa, ya), we determine the offset needed at each step to generate the next pixel position along the line path. We loop through this process steps times. If the magnitude of dx is greater than the magnitude of dy and xa is less than xb, the values of the increments in the x and y directions are 1 and m,
respectively. If the greater change is in the x direction, but xa is greater than xb, then the decrements - 1 and -m are used to generate each new point on the line. Otherwise, we use a unit increment (or decrement) in they direction and an x increment (or decrement) of l/m. 


## Algorithm 3
### [Bresenham's Line Algorithm](https://www.javatpoint.com/computer-graphics-bresenhams-line-algorithm)

This algorithm is used for scan converting a line. It was developed by Bresenham. It is an efficient method because it involves only integer addition, subtractions, and multiplication operations. These operations can be performed very rapidly so lines can be generated quickly. In this method, next pixel selected is that one who has the least distance from true line. It is faster as compared to DDA (Digital Differential Analyzer) because it does not involve floating point calculations like DDA Algorithm.

<!-- Difference between DDA & Bresenham's Algorithms -->

| `DDA Algorithm`	      |  `Bresenham's Line Algorithm` |
| :---                |   :---                      | 
| 1. DDA Algorithm use floating point, i.e., Real Arithmetic. |	1. Bresenham's Line Algorithm use fixed |point, i.e., Integer Arithmetic |
| 2. DDA Algorithms uses multiplication & division its operation | 2.Bresenham's Line Algorithm uses only subtraction and addition its operation |
| 3. DDA Algorithm is slowly than Bresenham's Line Algorithm in line drawing because it uses real arithmetic (Floating Point operation)	| 3. Bresenham's Algorithm is faster than DDA Algorithm in line because it involves only addition & subtraction in its calculation and uses only integer arithmetic. |
| 4. DDA Algorithm is not accurate and efficient as Bresenham's Line Algorithm.	| 4. Bresenham's Line Algorithm is more accurate and efficient at DDA Algorithm. |
| 5.DDA Algorithm can draw circle and curves but are not accurate as Bresenham's Line Algorithm | 5. Bresenham's Line Algorithm can draw circle and curves with more accurate than DDA Algorithm. |