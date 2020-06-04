import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

from dataProfile import DataProfile

def main():
  print('Hello world!')

  profile1 = DataProfile()
  profile1.addDataPoint(0.512)
  profile1.addDataPoint(0.890)
  profile1.addDataPoint(0.9002)

  profile1.printProfiles()

  x = np.linspace(0, 20, 100)  # Create a list of evenly-spaced numbers over the range
  plt.plot(x, np.sin(x))       # Plot the sine of each x point
  plt.show() 

  # fig, ax = plt.subplots()  # Create a figure containing a single axes.
  # ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  # Plot some data on the axes.
  
if __name__ == "__main__":
  main()