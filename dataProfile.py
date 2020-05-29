class DataProfile:
  profiles = []

  def __init__(self):
    print('created profile')

  def addDataPoint(self, point):
    self.profiles.append(point)

  def printProfiles(self):
    for x in self.profiles:
      print(x)