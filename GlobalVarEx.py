location="India" # defining global variables
class Institute:
 def display(self):
  global branch # declaring global variables
 
  branch="vashi" # defining global variables
  print("institute name Anudip")
  print("Location ",location )
  print("Branch ",branch) 
 
class Institute_branch:
 def display(self):
  print("institute name Coder")
  print("Location ",location ) 
  print("Branch ",branch) 
 
i=Institute()
i.display()
i1=Institute_branch();
i1.display()
print(location)#we can access global variables directly
