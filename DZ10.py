import random

l_st = []
l_en = []

for i in range(25):
    l_st.append(random.randint(20, 60))

i = 1

while (i + 1) != (len(l_st)) :
    if l_st[i] > l_st[i - 1] and l_st[i] > l_st[i + 1]:
        l_en.append(l_st[i])
        i += 1
    else:
        i += 1
print("Список чисел  :", l_st)
print("Кількість єлементів списку: ", len(l_st))
print("Елементи які більші за своїх сусідів  :", l_en)
print("Кількість елементів більших за своїх сусідів :", len(l_en))

# Дано перелік чисел. Визначте, скільки в цьому списку елементів, які більше двох своїх сусідів (ліворуч та праворуч),
# і виведіть кількість таких елементів. Останні елементи списку ніколи не враховуються, оскільки у них недостатньо сусідів.