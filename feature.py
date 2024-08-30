#searching the data
def linear_search(transactions,target):
  for tran in transactions:
    if tran['date']==target:
      return tran
  return 'transation not found'

#sorting the data
def sorting(transactions):
  n=len(transactions)
  for i in range(n):
    for j in range(0,n-1):
      if transactions[j]['amount']>transactions[j+1]['amount']:
        transactions[j],transactions[j+1]=transactions[j+1],transactions[j]
  return transactions

#adding data
def add_data(transactions):
  date=input('Enter the date: ')
  amount=int(input('Enter the amount: '))
  description=input('Enter the description:')
  a={'date':date,'amount':amount,'description':description}
  transactions.append(a)
  return transactions

#deleting data
def delete_data(transactions):
  date=input('Enter the date:')
  b=linear_search(transactions,date)
  transactions.remove(b)
  return transactions

def amount_add(transactions):
  year=input('Enter the year:')
  a=0
  for tran in transactions:
    if tran['date'][6::]==year:
      a+=tran['amount']
  return a


