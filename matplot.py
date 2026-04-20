import matplotlib.pyplot as plt

# Data
categories = ['A', 'B', 'C', 'D', 'E']
values = [10, 20, 15, 25, 18]

# Bar plot
plt.bar(categories, values, color='green')

# Labels and title
plt.title('Simple Bar Chart')
plt.xlabel('Categories')
plt.ylabel('Values')

# Show values on bars
for i, v in enumerate(values):
    plt.text(i, v + 1, str(v), ha='center')

plt.show()