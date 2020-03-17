def saddle_points(matrix):
	#Check lengths of all rows are equal
	rowLengths = {len(row) for row in matrix}
	if len(rowLengths) == 0:
		return []
	elif len(rowLengths) > 1:
		raise ValueError('The rows of the matrix must be the same length!')
	else:
		#Get a list of columns to match your list of rows
		colList = []
		for i in range(len(matrix[0])):
			col = []
			for row in matrix:
				col.append(row[i])
			colList.append(col)

		#Find maxes of each row and mins of each column- saddle point must be == max in its row, and == to min in its column
		rowMaxs = [max(row) for row in matrix]
		colMins = [min(col) for col in colList]	

		saddleList = []
		for i in range(len(matrix)):
			for j in range(len(colList)):
				if matrix[i][j] == rowMaxs[i] and matrix[i][j] == colMins[j]:
					saddleList.append({'row': i+1, 'column': j+1})

		return saddleList
				
		




		
	
