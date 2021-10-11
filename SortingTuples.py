Marks=[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
print('original marks list is: {}'.format(Marks))
Marks.sort(key=lambda x:x[1])
print('Sorted marks list is: {}'.format(Marks))