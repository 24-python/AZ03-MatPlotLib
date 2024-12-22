import matplotlib.pyplot as plt


# x = [1, 4, 5, 12, 15]
# y = [1, 2, 5, 6, 7]
#
# plt.plot(x, y)
# plt.title("My first plot")
# plt.xlabel("X")
# plt.ylabel("Y")
# plt.show()

# data = [7, 7, 8, 8, 8, 7, 9, 8, 9, 9, 9, 8, 8, 9, 7, 6, 6, 9, 6, 6]
#
# plt.hist(data, bins=3)
#
# plt.title("Кто как спит")
# plt.xlabel("часы сна")
# plt.ylabel("количество людей")
# plt.show()

x = [1, 4, 6, 7]
y = [3, 5, 8, 10]

plt.scatter(x, y)

plt.title("Тестовая диаграмма рассеяния")
plt.xlabel("Ось X")
plt.ylabel("Ось Y")
plt.show()
