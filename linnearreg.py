import numpy as np
import matplotlib.pyplot as plt

# Step 1: Collect height and weight data from the user
print("Enter height and weight data in the format 'height weight'. Type 'done' when finished:")

heights = []  # List to store height values
weights = []  # List to store weight values

while True:
    user_input = input("Enter height and weight: ").strip()
    if user_input.lower() == "done":
        break  # Stop input if the user types 'done'
    try:
        # Parse the input into two floats (height and weight)
        height, weight = map(float, user_input.split())
        heights.append(height)
        weights.append(weight)
    except ValueError:
        print("Invalid input. Please enter two numeric values separated by a space.")

# Step 2: Ensure there is enough data to proceed
if len(heights) < 2:
    print("Not enough data to perform regression. Please enter at least two data points.")
    exit()

# Step 3: Convert the height and weight data into numpy arrays
x = np.array(heights)  # Heights (independent variable)
y = np.array(weights)  # Weights (dependent variable)

# Step 4: Calculate the mean of x and y
mean_x = np.mean(x)
mean_y = np.mean(y)

# Step 5: Calculate the slope (m) and intercept (b)
numerator = np.sum((x - mean_x) * (y - mean_y))  # Sum of (x - mean_x) * (y - mean_y)
denominator = np.sum((x - mean_x) ** 2)         # Sum of (x - mean_x)^2
m = numerator / denominator                     # Slope of the regression line
b = mean_y - m * mean_x                         # Intercept of the regression line

# Step 6: Predict weights using the regression line
y_pred = m * x + b

# Step 7: Display results
print("\nLinear Regression Results:")
print(f"Equation of the line: y = {m:.2f}x + {b:.2f}")

# Step 8: Plot the data points and the regression line
plt.scatter(x, y, color="blue", label="Data Points")  # Scatter plot of the data
plt.plot(x, y_pred, color="red", label="Regression Line")  # Regression line
plt.xlabel("Height (cm)")  # Label for x-axis
plt.ylabel("Weight (kg)")  # Label for y-axis
plt.title("Manual Linear Regression")  # Title of the graph
plt.legend()  # Add legend
plt.grid(True)  # Add grid lines
plt.show()  # Display the graph
