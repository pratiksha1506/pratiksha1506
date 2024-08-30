#Combing the features into application
from feature import add_data,linear_search,delete_data,sorting,amount_add

#List of dict in variable
transactions=[{'date':'22-08-2024','amount':100,'description':'pani puri'},
             {'date':'23-08-2024','amount':450,'description':'book'},
             {'date':'24-08-2024','amount':400,'description':'dress'},
             {'date':'25-08-2024','amount':1000,'description':'college'}
             ]
flag=True
while flag:
  print('1.Adding the data')
  print('2.Searching data')
  print('3.sorting')
  print('4.deleting the data')
  print('5.Display')
  print('6.Exit')
  print('7.Sum of Amount')
  p=int(input('Enter the number which function should run: '))
  if p==1:
    print('-'*100)
    print('Adding the data')
    print(add_data(transactions))
    print('-'*100)
  elif p==2:
    print('-'*100)
    target=input('Enter the date: ')
    print('-'*100)
    print('Searching data')
    print('-'*100)
    print(linear_search(transactions,target))
    print('-'*100)
  elif p==3:
    print('-'*100)
    print('Sorting the Data')
    print('-'*100)
    print(sorting(transactions))
    print('-'*100)
  elif p==4:
    print('-'*100)
    print('Deleting the date')
    print('-'*100)
    print(delete_data(transactions))
    print('-'*100)
  elif p==5:
    print('-'*100)
    print('Display:',transactions) 
    print('-'*100)
  elif p==6:
    flag=False
    print('-'*100)
    print('The program is stoped')
    print('-'*100)
  elif p==7:
    print('-'*100)
    print('The sum of the Amount')
    print('-'*100)
    print(amount_add(transactions))
    print('-'*100)
  else:
    print('-'*100)
    print('Enter the right choice')
    print('-'*100)
