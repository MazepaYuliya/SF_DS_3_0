data = input().split()
n = int(data[0])
m = int(data[0])
news_list = [int(input()) for _ in range(n)]
news_dict_by_types = {type_number: [] for type_number in range(m)}
types_order = []
for news_index, type_number in enumerate(news_list):
    news_dict_by_types[type_number].append(news_index)
    if type_number not in types_order:
        types_order.append(type_number)
    
result = []
ind = 0
last_type = m+1
while ind < n:
    for type_number in types_order:
        if type_number == last_type:
            ind = n
            break
        if news_dict_by_types[type_number]:
            result.append(news_dict_by_types[type_number].pop(0))
            ind += 1
            last_type = type_number
    
print(' '.join(map(str, result)))