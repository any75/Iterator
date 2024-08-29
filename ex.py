# def fruit_generate():
#     # Создадим итератор при помощи генератора.
#     for item in ['apple', 'banana', 'cherry']:
#         yield item
def iterator_my(string):
    for i in string:
        yield i

x = iterator_my('Мама ')

for r in range(7):
    print(f'{next(x)}{r}')
    # print(x)

# letter = next(x)
# print(letter)