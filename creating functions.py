def readmat (nrow=2, ncol=2):
    mat = [[0.0]* ncol for i in range(nrow)]
    for i in range(nrow):
        for j in range(ncol):
            mat[i][j] = float(input("{} {}:".format(i,j)))
    return mat

def transpose(mat,dim):
    for i in range(dim):
        for j in range(i+1,dim):
            temp = mat[i][j]
            mat[i][j] = mat[j][i]
            mat[j][i] = temp
            #print(i,j)
    return

def printmat(mat,nrow=2,ncol=2):
    for i in range(nrow):
        for j in range(ncol):
            print("{:0.3f}".format(mat[i][j]),end = " ")
        print()
    

mat = []
mat = readmat(3,3)
print(mat)
printmat(mat,3,3)
print("Transpose:\n\n\n")
transpose(mat,3)
printmat(mat,3,3)
