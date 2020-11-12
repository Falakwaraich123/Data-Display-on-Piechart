from matplotlib import pyplot as plt
import numpy as np

# Creating dataset
labels = ['Cookies', 'Jellybean', 'Milkshake', 'Cheesecake']
cars = ['WINDOW-OS', 'ANDROID-OS', 'LINUX-OS',
        'MAC-OS']

data = [77.74, 74.43, 65.5,53.33]

# Creating plot
fig = plt.figure(figsize=(10, 7))
plt.pie(data, labels=cars)

# show plot

plt.show()