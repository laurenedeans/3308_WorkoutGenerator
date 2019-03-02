
def main():
  print() 
  print("WELCOME TO GIT-FIT!")
  print() 
  print("This program is designed to help you choose and create a workout centered on your goal.")
  input("Press Enter to continue") 
  print()
  print("The possible goals for you to choose are:")
  print("1. lose weight")
  print("2. gain strengt````````````````````````````````````````h")
  print("3. gain muscle mass")
  print("4. look like <insert famous celebrity>")
  print() 
  choose()


def choose():
  choice = int(input("What is your main goal or reason for wanting to exercise? "))
  if choice == 1:
    choice = "lose weight"
    print()  
    print("The type of workout you will most likely need is aerobic. Types of exercises might include step workouts, bicycling, or jogging.")
    print() 
    answer(choice)
  elif choice == 2:
    choice = "gain strenth"
    print()  
    print("The type of workout you will most likely need is a mix of aerobic and anaerobic. Types of exercises might include weightlifting, sit-ups, pullups,.. all in quick succession.")
    answer(choice)
  elif choice == 3:
    choice = "gain muscle mass"
    print()  
    print("The type of workout you will most likely need is anaerobic. Types of exercises might include free weight with short quick repititions.")
    answer(choice)
  elif choice == 4:
    print()  
    print("Wouldn't we all! You're going to need a plastic surgeon for that! Ha, ha, ha! Please choose one of the first three!")
    print()  
    choose()
  else:
    oops()
    choose()


def answer(chose):
  ans = input("Does this sound like something you would like? (Y)es or (N)o? ")
  ans = ans.upper()
  if ans == "Y":
    workout(chose)
  elif ans == "N":
    print()  
    print("I'm sorry to hear that. Let's pick something else, then.")
    choose()
  else:
    oops()  
    answer(chose)
  
def workout(chose):
  print() 
  print("The following are different areas of your body that you can focus on. ")
  print() 
  print("1. Legs")
  print("2. Abdomin")
  print("3. Arms")
  print()  
  bodypart = int(input("What area of your body are you most interested in working on? "))
  if bodypart == 1:
    bodypart = "legs"
  elif bodypart == 2:
    bodypart = "abdomin"
  elif bodypart == 3:
    bodypart = "arms"
  else:
    oops() 
    workout(chose)
  exercise(chose, bodypart)

def exercise(chose, bodypart):
  print()  
  print("A list of exercises to " + chose + " including " + bodypart + " would be listed here.")

def oops():
  print()  
  print("I'm sorry I don't understand. Could you please enter an option again?")
  print()
  

main()

