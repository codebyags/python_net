import random

# Математика для матриц, линейная алгебра... 
# i - Строки
# j - Колонки

# Проверяет что матрица в порядке, не кривая.
def check_matrix(matrix):

	if type(matrix) is not list:
		return False

	first_col_length = False;
	
	for row in matrix:
		if first_col_length == False:	
			first_col_length = len(row)
		
		if len(row) != first_col_length:
			return False

	return True
	
# Печатаем матрицу
def print_matrix(matrix):

	if check_matrix(matrix) == False:
		print("Матрица кривая, ни как не распечатать.", matrix)
		return
	
	for row in matrix:
		str_row = "|"
		for col in row:
			str_row += str(col) + "|" 
		print(str_row)
		print("-" * (len(row)*2+1) )

# Получаем раззмеры матрицы	
# @return [Столбцов J, Строк I]
def get_matrix_size(matrix):
	return [len(matrix[0]), len(matrix)]
	
# Возможно ли сложить ли вычитать матрицы	
# Можно складывать матрицы только где i1 = i2 и j1 = j2 
def is_can_add_or_sub(matrix_1, matrix_2):
	martix_1_size = get_matrix_size(matrix_1)
	martix_2_size = get_matrix_size(matrix_2)
	
	if martix_1_size[0] == martix_2_size[0] and martix_1_size[1] == martix_2_size[1]:
		return True
	else:
		return False

# Сложение и вычитание матриц "топорно"
def add_or_sub_matrix(matrix_1, matrix_2, operation):
	if is_can_add_or_sub(matrix_1, matrix_2) == False:
		return False
	
	size = get_matrix_size(matrix_1)
	
	i = size[1];
	j = size[0];
	
	result_matrix = []
	
	row_iterator = 0
	while row_iterator < i:
		result_row = []
		col_iterator = 0
		
		while col_iterator < j:
			
			if operation == "add":
				res = matrix_1[row_iterator][col_iterator] + matrix_2[row_iterator][col_iterator]
			else:
				res = matrix_1[row_iterator][col_iterator] - matrix_2[row_iterator][col_iterator]
				
			result_row.append(res)
			col_iterator += 1

		result_matrix.append(result_row)
		row_iterator += 1
	
	return result_matrix

# Сложение матриц
def add_matrix(matrix_1, matrix_2):
	return add_or_sub_matrix(matrix_1, matrix_2, 'add')
	
# Вычитание матриц	
def sub_matrix(matrix_1, matrix_2):
	return add_or_sub_matrix(matrix_1, matrix_2, 'sub')

# Можно ли умножать эти марицы
def is_can_mul_matrix(matrix_1, matrix_2):
	size_matrix_1 = get_matrix_size(matrix_1)
	size_matrix_2 = get_matrix_size(matrix_2)
	
	if size_matrix_1[0] == size_matrix_2[1]:
		return True
		
	print("Умножение невзоможно")
	return False
	
# Умножение матрицы	
def mul_matrix(matrix_1, matrix_2):
	if is_can_mul_matrix(matrix_1, matrix_2) == False:
		
		return False
		
	size_matrix_1 = get_matrix_size(matrix_1)
	size_matrix_2 = get_matrix_size(matrix_2)
	
	result_matrix = []
	result_matrix_i = size_matrix_1[1]
	result_matrix_j = size_matrix_2[0]
	i = 0
	
	while i < result_matrix_i:
		j = 0
		result_col_matrix = []
		while j < result_matrix_j:
			ij = 0
			res = 0
			#print("R_COORD:" + str(i) + "," + str(j))
			while ij < size_matrix_1[0]:
				res += matrix_1[i][ij] * matrix_2[ij][j]
				#print("" + str(matrix_1[i][ij]) + " * " + str( matrix_2[ij][j]))
				ij += 1
			result_col_matrix.append(res)
			j += 1
			
		result_matrix.append(result_col_matrix)
		i += 1

	return result_matrix
	
# Создать случайно наполненую матрицу со значениями от 0 до 1
# Если cols = 1, считаем что это вектор-колонка
# Если rows = 1, считаем что это вектор-строка 
def create_random_matrix(rows, cols):
	result_matrix = []
	i = 0
	while i < rows:
		j = 0
		result_col_matrix = []
		while j < cols:
			res = random.random()
			result_col_matrix.append(res)
			j += 1
		result_matrix.append(result_col_matrix)
		i += 1
	return result_matrix

# Применить функцию к каждому элемнту матрицы
def map_matrix(matrix, function):
	matrix_size = get_matrix_size(matrix)
	result_matrix = []
	i = 0
	while i < matrix_size[1]:
		j = 0
		result_col_matrix = []
		while j < matrix_size[0]:
			res = function(matrix[i][j])
			result_col_matrix.append(res)
			j += 1
		result_matrix.append(result_col_matrix)
		i += 1
	return result_matrix

# Экспонента
def exp(value):
	return 2.7182818284 ** value

# Сумма элементов матрицы
def sum_matrix(matrix):
	matrix_size = get_matrix_size(matrix)
	result_sum = 0
	i = 0
	while i < matrix_size[1]:
		j = 0
		while j < matrix_size[0]:
			result_sum += matrix[i][j]
			j += 1
		i += 1
	return result_sum


# Пытаемся нейро-классификатор
# Параметр однослойной сети
INPUT = 4 	# Четрыре входа
LAYER = 10 	# Скрытые нейроны
OUT = 2 	# Выходные нейроны

# Рандомные значения нейронной сети, увы пока без обучения
# TODO: конструктор неройнной сети
INPUT_VECTOR = create_random_matrix(1, INPUT)   # Входной вектор-строка

LAYER_1 = create_random_matrix(INPUT, LAYER) 	# Скрытый слой
BIAS_1 = create_random_matrix(1, LAYER) 		# Смещения

LAYER_2 = create_random_matrix(LAYER, OUT)		# Выход
BIAS_2 = create_random_matrix(1, OUT) 		    # Смещения выхода


# Функция активации нейрона
def relu(value): 
	if value < 0:
		value = 0
	return value

# Делаем выходные нейроны со значениями 0 до 1
def softmax(matrix):
	matrix = map_matrix(matrix, exp)
	return map_matrix(matrix, lambda value: value / sum_matrix(matrix))
	
# Выполнить вычисление
def predict(INPUT_VECTOR):
	RESUTL_LAYER_1 = add_matrix(mul_matrix(INPUT_VECTOR, LAYER_1), BIAS_1)
	RESUTL_LAYER_1_HIDDEN = map_matrix(RESUTL_LAYER_1, relu)
	RESUTL_LAYER_2 = add_matrix(mul_matrix(RESUTL_LAYER_1_HIDDEN, LAYER_2), BIAS_2)
	RESULT = softmax(RESUTL_LAYER_2)
	print_matrix(RESULT);
	
predict(INPUT_VECTOR)

input('Press ENTER to exit')