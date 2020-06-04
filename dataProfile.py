class DataProfile:
  profiles = []
  header = ''
  # Should header be an individual string,
  # or a conjuncture of all the subfields?

  def __init__(self):
    print('created profile')

  def addDataPoint(self, point):
    self.profiles.append(point)

  def printProfiles(self):
    for x in self.profiles:
      print(x)