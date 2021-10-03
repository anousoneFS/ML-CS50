row, col = (0,2)
dadicate = [
    ('Up', (row-1, col)),
    ('Down', (row+1, col)),
    ('Right', (row, col+1)),
    ('Left', (row, col-1))
]

walls = [[True, True, False, False, True], [ False, False, False, True, False], [True, False, False, True, True]]

a = []
for i in dadicate:
    r,c  = i[1]
    if r,c in walls:
        a.append(i)
# return a

for i in a:
    print(f'state = {a[1]}')