import copy
from fractions import frac
class matrix:
    def __init__(self, i, j):
        if isinstance(i, int) and isinstance(j, int):
            self.__i = i
            self.__j = j
            self.__list1 = []  #__list1 contains list of the rows
    
    def __str__(self):
        string1 = ""
        for x in range(len(self.__list1)):
            string1 = string1 + str(self.__list1[x]) + "\n"
        return string1
    
    def __getitem__(self, key):
        return self.__list1[key]

    def insertRow(self, *args):
        """
        This function is used to insert a row in the matrix.
        It can only add if the matrix doesn't have the complete number of rows indicated in the matrix initiation 
        """
        if len(self.__list1) < self.__i: #Checking if there is free space to add more rows
            if len(args) == self.__j:   #Checking if no. of elements entered is no. of columns
                self.__list1.append(list(args))
            elif len(args)==1 and isinstance(args[0], list):
                self.__list1.append(args[0])
            else:
                print("Enter only "+str(self.__j)+" numbers. Only "+str(self.__j)+" columns or enter a list")
        else:
            print("Only "+str(self.__i)+" rows allowed")
            
    def __add__(self, other):
        """
        This function adds matrices.
        The order of the matrices has to be same
        """
        if len(self.__list1) == len(other.__list1) and self.__j == other.__j:
            matNew = matrix(self.__i, self.__j)
            for x in range(self.__i):
                listNew = []
                for y in range(self.__j) :
                    listNew.append(self.__list1[x][y] + other.__list1[x][y])
                matNew.__list1.append(listNew)
            return matNew
        else:
            print("You can add only matrices with the same order")
            
    def __sub__(self, other):
        """
        This function subtracts matrices.
        The order of the matrices has to be same
        """
        if len(self.__list1) == len(other.__list1) and self.__j == other.__j:
            matNew = matrix(self.__i, self.__j)
            for x in range(self.__i):
                listNew = []
                for y in range(self.__j) :
                    listNew.append(self.__list1[x][y] - other.__list1[x][y])
                matNew.__list1.append(listNew)
            return matNew
        else:
            print("You can subtract only matrices with the same order")
    
    def __mul__(self, other):
        """
        This method is used for scalar multiplication of a matrix
        """
        if isinstance(self, matrix) and (isinstance(other, float) or isinstance(other, int) or isinstance(other, frac)):
            matrixNew = copy.deepcopy(self)
            for i in range(len(self.__list1)):
                for j in range(self.__j):
                    matrixNew .__list1[i][j] = matrixNew.__list1[i][j] * other
            return matrixNew
        else:
            print("Error: For matrix scalar multiplication, put a matrix and and integer or a float. Do not put any other data type.")
    
    def __rmul__(self, other):
        """
        This is similar to __mul__ function but it allows for a number times the matrix.
        """
        if isinstance(self, matrix) and (isinstance(other, float) or isinstance(other, int) or isinstance(other, frac)):
            matrixNew = copy.deepcopy(self)
            for i in range(len(self.__list1)):
                for j in range(self.__j):
                    matrixNew.__list1[i][j] = matrixNew.__list1[i][j] * other
            return matrixNew
        else:
            print("Error: For matrix scalar multiplication, put a matrix and and integer or a float. Do not put any other data type.")
 
    def __pow__(self, other):
        """
        This method is used to find the dot product of matrices
        The number of columns of the first matrix should be equal to the number of rows in the second matrix
        """
        if self.__j == len(other.__list1):
            matNew = matrix(len(self.__list1), other.__j)
            for x in range(len(self.__list1)):  #For traversing through every row in first matrix
                listNew = []
                for y in range(other.__j):  #For traversing through each column in second matrix
                    sum1 = 0
                    for z in range(self.__j):   #For traversing through each element in a column of second matrix
                        sum1 = sum1 + (self.__list1[x][z] * other.__list1[z][y])
                    listNew.append(sum1)
                matNew.__list1.append(listNew)
            return matNew
        else:
            print("The number of columns of the first matrix must be equal to the number of rows of the second matrix")
    
    def transpose(self):
        """
        This method finds the transpose of the matrix
        """
        matNew = matrix(self.__j, len(self.__list1))
        for x in range(self.__j):
            listNew = []
            for y in range(len(self.__list1)):
                listNew.append(self.__list1[y][x])
            matNew.__list1.append(listNew)
        return matNew

    def __deter2(self):
        """
        This method is used to find the determinant of a 2x2 matrix
        """
        if len(self.__list1) == self.__j:
            determinant = 0
            for i in range (self.__j):
                determinant = determinant + ((-1)**i)*(self.__list1[0][i] * self.__list1[1][(i+1) %2])
            return determinant
        else:
            print("It should be a 2x2 matrix only!!")
            return

    def determinant(self):
        """
        This method is used to find determinant of a nxn matrix
        """
        if len(self.__list1) == self.__j:  #Checking if it is a sqaure matrix only
            matrixNew = copy.deepcopy(self) #making a copy of the matrix passed
            determinant = 0         #For a single matrix...this will add up 
            if self.__j == 2:
                determinant = determinant + self.__deter2() #If it is a 2x2 matrix...call  __deter2
                return determinant
            else:
                for i in range(matrixNew.__j):
                    temporary_matrix = copy.deepcopy(matrixNew)
                    del temporary_matrix.__list1[0]                 #To delete the top row and a column
                    for j in range(len(temporary_matrix.__list1)):
                        del temporary_matrix.__list1[j][i]
                    temporary_matrix.__j = temporary_matrix.__j - 1     #We deleted a column
                    determinant = determinant + ( ((-1)**i) * matrixNew.__list1[0][i] * temporary_matrix.determinant() )
                return determinant
        else:
            print("It should be a sqaure matrix only!!")
            return

    def adjoint(self):
        """
        This method is used to find the adjoint of a nxn matrix
        E.g:
            [3 1 -1]          [2 -1 -2]
            [2 -2 0]    ->    [2 -2 -2]
            [1 2 -1]          [6 -5 -8]
        """
        if len(self.__list1) == self.__j:
            adjoint = matrix(len(self.__list1), self.__j)     #Making the new adjoint matrix
            if (len(self.__list1) == 2):
                adjoint.insertRow(self.__list1[1][1], -1*self.__list1[0][1])
                adjoint.insertRow(-1*self.__list1[1][0], self.__list1[0][0])
            else:
                for i in range(len(self.__list1)):      #For every row in matrix passed in function
                    temporaryMatrix = copy.deepcopy(self)       #Making copy of the passed matrix in function
                    del temporaryMatrix.__list1[i]      #Deleting a row according to loop value of i
                    addList = []    #Making a list of numbers to add to the adjoint
                    for j in range(temporaryMatrix.__j):    #For every column in the matrix passed after deleting a row
                        temporaryMatrix2 = copy.deepcopy(temporaryMatrix)   #Making a second copy for second for loop
                        for z in range(len(temporaryMatrix.__list1)):       #For every row in the matrix passed after deleting a row
                            del temporaryMatrix2.__list1[z][j]          #Deleting a column from the 2nd temp matrix
                        temporaryMatrix2.__j = temporaryMatrix2.__j - 1     #Since we deleted a column
                        addList.append( ((-1)**(i+j))*temporaryMatrix2.determinant())   #Adding the determinant of the 2nd temp matrix to list to numbers to add to adjoint
                    adjoint.__list1.append(addList)     #Adding the list values to the adjoint to add a row
                adjoint = adjoint.transpose()       #Transposing to get final matrix for adjoint
            return adjoint
        else:
            print("It should be a sqaure matrix only!!")
            return
            
    
    def inverse(self):
        determinant = self.determinant()
        #print("Determinant =",determinant)
        if determinant == 0:
            return "Inverse does not exist!!"
        adjoint = self.adjoint()
        #print("Adjoint =")
        #print(adjoint)
        inverse = adjoint * frac("1/"+str(determinant))
        return inverse