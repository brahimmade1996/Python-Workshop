def list2tuple(List):
    '''
Turns a 2D list in to a 2D tuple
    '''
    list_of_tuples=[tuple(row) for row in List]
    return tuple(list_of_tuples)

def dotproduct(l1,l2):
    if len(l1)!=len(l2):
        raise Exception('Length of to vectors must be equal')
    dot=0
    for i in range(len(l1)):
        dot+= l1[i]*l2[i]
    return dot

class Matrix():
    '''
This class is for computing simple matrixs ops
'''
    def validate_rows(self):
        length_row=len(self.rows[0])
        for row in self.rows:
            if len(row)!=length_row:
                raise Exception("rows must be of same lengths")

    def __init__(self,List):
        self.rows=list2tuple(List)
        self.validate_rows()

        
        
        # (tuple(row) for row in List)

    def count_rows(self):
        '''
counts the number of rows
'''
        return len(self.rows)

    def count_columns(self):
        '''
counts the number of columns
        '''
        return len(self.rows[0])

    def __rmul__(self,num):
        matrix=[]
        for row in self.rows:
            mulrow=[]
            for index in row:
               mulrow.append(index*num)
            matrix.append(mulrow)

        return Matrix(matrix)

    def __mul__(self,num):
        matrix=[]
        for row in self.rows:
            mulrow=[]
            for index in row:
               mulrow.append(index*num)
            matrix.append(mulrow)

        return Matrix(matrix)
        
    def get_column(self,index):
        """ returns the index column """

        column=[]
        for row in self.rows:
            column.append(row[index])

        return column

    
    

