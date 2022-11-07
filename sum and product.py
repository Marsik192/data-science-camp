from collections import Counter

#функція яка розкладає s на доданки а, та s-a
def additions_of_sum(s):
    return [(a,s-a) for a in range(2,int(s/2+1))]

# Генеруємо всі можливі пари чисел від 2 до 99 включно
all_pairs = set((a,b) for a in range(2,100) for b in range(a+1,100) if a+b<100)

# Кількість можливих пар
product_amount = Counter(c*d for c,d in all_pairs)

# Знаходимо унікальні пари (зустрічаються 1 раз)
unique_products = set((a,b) for a,b in all_pairs if product_amount[a*b]==1)

# Знаходимо пари для яких всі можливі розклади суми, мають не унікальні добутки, тобто зустрічаються 2 або більше разів
sum_pairs = [(a,b) for a,b in all_pairs if
    all((x,y) not in unique_products for (x,y) in additions_of_sum(a+b))]

# Серед s_pairs знаходимо унікальні добутки
product_amount = Counter(c*d for c,d in sum_pairs)
product_pairs = [(a,b) for a,b in sum_pairs if product_amount[a*b]==1]

# Із p_pairs знаходимо унікальні доданки, і вивдоимо їх
sum_amount = Counter(c+d for c,d in product_pairs)
result = [(a,b) for a,b in product_pairs if sum_amount[a+b]==1]
print(result)