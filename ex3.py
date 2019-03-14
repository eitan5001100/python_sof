def row(row_num,mat):
    r=mat[row_num]
    first= r[0]

    for i in r:
        if first!=i:
            return False
        return True


def col(col_num,mat):
    first=mat[0][col_num]

    for i in range(3):
        if first!=mat[i][col_num]:
            return False
        return True

def slant(mat):
    slant1=mat[0][2]
    winner=slant1
    for i in range(3):
        if slant1!=mat[i][i]:
            winner=False
            break
    return winner







game=[[1,2,0],
      [2,1,0],
      [2,1,1]]
winner=False

for i in range(3):
    if col(i,game):
        print(str(game[0][i])+" won")
        winner=True
        break
    if row(i,game):
        print(str(game[i][0]) + " won")
        winner = True
        break
if  slant(game)!=False:
    print(slant(game) + " won")
    winner = True
if winner==False:
    print("tie")