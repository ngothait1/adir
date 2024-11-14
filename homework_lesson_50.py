import pandas as pd

df = pd.read_csv("C:\\Users\\adirv\\Videos\\קורס תכנות עם נדב גוטהייט\\קורס פייתון\\קבצים\\advance_files\\customer_data.csv")

# 1
list_of_purchase = []
for index, row in df.iterrows():
    purchase_amount = row["purchase_amount"]
    list_of_purchase.append(purchase_amount)
list_of_purchase.sort(reverse=True)
print(list_of_purchase[0])

# 2
total_sum_ages = 0
count_numbers = 0
for index, row in df.iterrows():
    age = row["age"]
    total_sum_ages += age
    count_numbers += 1
average = total_sum_ages / count_numbers
print(average)

# 3
total_income = 0
for index, row in df.iterrows():
    if index > 8348:
        break
    income = row["income"]
    total_income += income
print(total_income)

# 4
dict_of_products_counter = {}
for index, row in df.iterrows():
    product_category = row["product_category"]
    if product_category in dict_of_products_counter:
        dict_of_products_counter[product_category] += 1
    else:
        dict_of_products_counter[product_category] = 1
print(dict_of_products_counter)

# 5
total_entries = 0
for index, row in df.iterrows():
    satisfaction_score = row["satisfaction_score"]
    if satisfaction_score > 7:
        total_entries += 1
print(total_entries)