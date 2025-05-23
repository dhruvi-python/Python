a = 10
b = 5
print(a+b)
print(4>6==False)
print(bool(4>6)) 

vanshika='yes'
kavya='no'
 
if vanshika == 'yes'and kavya == 'no':
   print("you will be a model")
elif vanshika == 'yes' and kavya == 'yes':
   print("she is a girl")
elif vanshika == 'yes'and kavya == 'no':
   print("she is not a girl") 
else:
 print("both are girl")

  #nested if
 name = 'ruhi'
 company='true'
if ('name' =='True'):
       if(company == 'true'):
          print('passed')
       else:
          print('not pass')
else:
          print('both off')

   #python lists
list = ["auto","bike","car"]
print(len(list))    

   #type()
list = ["fan","light","room"]
print(type(list))

   #the list()constructor
list1 = (("tomato","onion","potato"))
print(list1)

# Example: Break when a specific number is found
numbers = [1, 3, 5, 7, 9, 11]

for num in numbers:
    print(f"Checking number: {num}")
    if num == 7:
        print("Number 7 found, breaking the loop.")
        break
        

print("Loop ended.")
