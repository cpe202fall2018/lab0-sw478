def weight_on_planets():
   print("What do you weigh on earth? ", end = "")
   x = int(input())
   print("\nOn Mars you would weigh " + str(x*0.38) + " pounds.")
   print("On Jupiter you would weigh " + str(x*2.34) + " pounds.")
   
if __name__ == '__main__':
   weight_on_planets()