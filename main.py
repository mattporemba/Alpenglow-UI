from dataProfile import DataProfile

def main():
  print('Hello world!')

  profile1 = DataProfile()
  profile1.addDataPoint(0.512)
  profile1.addDataPoint(0.890)
  profile1.addDataPoint(0.9002)

  profile1.printProfiles()
  
if __name__ == "__main__":
  main()