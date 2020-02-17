class Matrix:
	def __init__(self, matrix_string):
		self.matrix2D = []
		rowsArray = matrix_string.split('\n')
		for row in rowsArray:
			self.matrix2D.append(row.split())
		#Notice matrix2D is a 2D array- a list of lists, where each element
		#is a row of the matrix
		self.numRows = len(rowsArray)

		#The following checks to make sure that the rows are all the same
		#length- if they're not, that indicates that there are some column
		#lengths that are different than others (invalid matrix)
		rowLengths = set()
		for row in self.matrix2D:
			rowLengths.add(len(row))
		if len(rowLengths) <= 0:
			raise ValueError('This matrix is empty!')
		elif len(rowLengths) > 1:
			raise ValueError('All rows must be the same length!')
		else:
			self.numCols = rowLengths.pop()
		
		#Up until now, all the elements of our matrix are strings! Convert
		#them to integers.
		for i in range(self.numRows):
			for j in range(self.numCols):
				self.matrix2D[i][j] = int(self.matrix2D[i][j])		

	def row(self, index):
		return self.matrix2D[index - 1]

	def column(self, index):
		return [row[index - 1] for row in self.matrix2D]


#Testing
#matrix1 = Matrix('1 2\n3 4')
#print('matrix 1 num cols:', matrix1.numCols)
#print('matrix 1 num rows:', matrix1.numRows)	
#print('matrix 1 row 1:', matrix1.row(1))
#print('matrix 1 row 2:', matrix1.row(2))
#print('matrix 1 col 1:', matrix1.column(1))
#print('matrix 1 col 2:', matrix1.column(2))

#matrix2 = Matrix('1 2\n3')
	
