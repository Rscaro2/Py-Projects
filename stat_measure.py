# Name: Rishi Scaro, Date: 10/15/2026, Description: This program uses given data points to calculate min, max, mean, and standard deviation. 

data_points = []

while True: 
    point = float(input("Enter a data point (-999 to stop) : "))
    if point == -999:
        break
    data_points.append(point)
    if len(data_points) == 0:
        print("No valid data points entered.")
    else:
        total = 0
        count = 0 
        minimum = data_points[0]
        maximum = data_points[0]
    for point in data_points:
        total += point
        count += 1
        if point < minimum:
            minimum = point
        if point > maximum:
            maximum = point
    mean = total / count
    sum_squared_diff = 0
    for point in data_points:
        sum_squared_diff += (point - mean) ** 2
    if count > 1:
        variance = sum_squared_diff /(count - 1)
    else: 
        variance = 0
        
    std_dev = variance ** 0.5

print()

print("Number of data points:", count)
print("Mean:", mean)
print("Minimum:", minimum)
print("Maximum:", maximum)
print("Standard Deviation:", format(std_dev, ".2f"))


