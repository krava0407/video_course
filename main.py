data1 = r"C:\Users\Тол\PycharmProjects\test_site\test_file_42.txt"
data2 = r"C:\fakepath\test_file_42.txt"

name1 = data1.split("\\")[-1]
print(name1)
name2 = data2.split("\\")[-1]
print(name2)