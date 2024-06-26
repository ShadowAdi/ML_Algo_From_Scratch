import pandas as pd

import matplotlib.pyplot as plt

data=pd.read_csv("study_time_marks.csv")

def mse(m,b,points):
    total_error=0
    for i in range(len(points)):
        x=points.iloc[i].StudyTime
        y=points.iloc[i].Marks
        total_error+=(y-(m*x+b))**2
    return total_error/float(len(points))


def gradient_descent(m_now,b_now,points,L):
    m_gradient=0
    b_gradient=0

    n=len(points)

    for i in range(n):
        x=points.iloc[i].StudyTime
        y=points.iloc[i].Marks

        m_gradient=-(2/n)*x*(y-(m_now*x+b_now))
        b_gradient=-(2/n)*(y-(m_now*x+b_now))

    m=m_now-m_gradient*L
    b=b_now-b_gradient*L
    return m,b


m=0
b=0
L=0.001
epochs=1000

for i in range(epochs):
    if i%50==0:
        print(f"Epoch: {i}")
    m,b=gradient_descent(m,b,data,L)

print(m,b)

plt.scatter(data.StudyTime,data.Marks)
plt.plot(list(range(0,80)),[m*x+b for x in range(0,80)],color="red")
plt.xlabel("Study Time")
plt.ylabel("Marks")
plt.title("Study Time vs Marks with Linear Regression Line")
plt.show()

mean_squared_error=mse(m,b,data)
print("Mean Squared Error: ",mean_squared_error)