def is_valid_universe(matrix):
    if len(matrix)==0 or len(matrix[0])==0:
        return False   
    for row in range(len(matrix)):
        if len(matrix[row])!=len(matrix[row-1]) or type(matrix[row])!=list:
            return False
        for num in matrix[row]:
            if num not in [0, 1]:
                return False
    return True

def create_copy(matrix):
    new_matrix = []
    for row in matrix:
        new_row = []
        for num in row:
            new_row.append(num)
        new_matrix.append(new_row)
    return new_matrix

def universe_to_str(matrix):
    new_matrix= create_copy(matrix)
    rep= "+" + "-"*len(new_matrix[0]) + "+\n"
    for row in new_matrix:
        for num in range(len(row)):
            if row[num]==0:
                row[num]=" "
            if row[num]==1:
                row[num]="*"
        rep+= "|"+"".join(row)+"|\n"
    rep+= "+" + "-"*len(new_matrix[0]) + "+"
    return rep

def count_live_neighbors(matrix, x, y):
    new_matrix= create_copy(matrix)
    counter= 0
    for i in [x-1, x, x+1]:
        if i in[-1, len(new_matrix)]:
            continue
        for j in [y-1, y, y+1]:
            if j in[-1, len(new_matrix[0])]:
                continue
            if new_matrix[i][j]==1:
                counter+=1
    if new_matrix[x][y]==1:
        counter-=1
    return counter

def get_next_gen_cell(matrix, x, y):
    live_neighbors=count_live_neighbors(matrix, x, y)
    if live_neighbors<2 or live_neighbors>3 :
        return 0
    if live_neighbors==3:
        return 1
    return matrix[x][y]

def get_next_gen_universe(matrix):
    new_matrix= create_copy(matrix)
    for row in range (len(matrix)):
        for num in range(len(matrix[0])):
            new_matrix[row][num]=get_next_gen_cell(matrix, row, num)
    return new_matrix

def get_n_generations(matrix, n):
    new_matrix= create_copy(matrix)
    if type(matrix)!= list or type(n)!= int:
        raise TypeError
    if is_valid_universe(matrix)== False:
        raise ValueError
    if n<=0:
        raise ValueError
    
    m= 1
    while m<n:
        new_matrix= get_next_gen_universe(new_matrix)
        if matrix== new_matrix:
            break
        m+=1
    new_matrix= create_copy(matrix)
    list_of_m= []
    for num in range(m):
        list_of_m.append(universe_to_str(new_matrix))
        new_matrix= get_next_gen_universe(new_matrix)
    return list_of_m
