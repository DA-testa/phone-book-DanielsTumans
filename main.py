n = int(input())
phone_book = {}
for i in range(n):
    query = input().split()
    if query[0] == 'add':
        phone_book[query[1]] = query[2]
    elif query[0] == 'del':
        phone_book.pop(query[1], None)
    else:
        print(phone_book.get(query[1], 'not found'))
        
