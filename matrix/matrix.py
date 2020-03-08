class Matrix:
	def __init__(self, matrix_string):
		self.matrix2D = [[int(x) for x in row.split()] for row in matrix_string.split('\n')]		

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

	def row(self, index):
		return [x for x in self.matrix2D[index - 1]]

	def column(self, index):
		column = [row[index - 1] for row in self.matrix2D]
		return [x for x in column]

