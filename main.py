import numpy as np

def create_matrix(rows, cols):
    matrix = [[0 for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            while True:
                value = input(f"Digite o valor para A[{i}][{j}]: ")
                try:
                    matrix[i][j] = float(value.replace(",", "."))
                    break
                except ValueError:
                    print("Valor inválido. Por favor, tente novamente.")
    return matrix

def add_matrices(A, B):
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])

    if rows_A != rows_B or cols_A != cols_B:
        raise ValueError("As matrizes devem ter o mesmo tamanho para serem somadas.")

    result = [[A[i][j] + B[i][j] for j in range(cols_A)] for i in range(rows_A)]
    return result

def subtract_matrices(A, B):
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])

    if rows_A != rows_B or cols_A != cols_B:
        raise ValueError("As matrizes devem ter o mesmo tamanho para serem subtraídas.")

    result = [[A[i][j] - B[i][j] for j in range(cols_A)] for i in range(rows_A)]
    return result

def multiply_matrices(A, B):
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])

    if cols_A != rows_B:
        raise ValueError("O número de colunas da primeira matriz deve ser igual ao número de linhas da segunda matriz.")

    result = [[sum(a * b for a, b in zip(row_A, col_B)) for col_B in zip(*B)] for row_A in A]
    return result

def transpose_matrix(A):
    return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]

def inverse_matrix(A):
    try:
        result = np.linalg.inv(np.array(A))
        return result
    except np.linalg.LinAlgError:
        print("A matriz não é invertível.")
        return None

def determinant_matrix(A):
    return np.linalg.det(A)

def format_matrix(matrix):
    return "\n".join([" ".join(map(lambda x: str(x).replace('.', ''), row)) for row in matrix])

while True:
    print("\nEscolha sua opção:")
    print("1 - Somar duas matrizes")
    print("2 - Subtrair duas matrizes")
    print("3 - Matriz inversa")
    print("4 - Multiplicar duas matrizes")
    print("5 - Matriz transposta")
    print("6 - Calcular determinante de matriz")
    print("7 - Sair")

    choice = int(input("Sua opção: "))

    if choice == 1:
        rows = int(input("Digite o número de linhas da matriz A: "))
        cols = int(input("Digite o número de colunas da matriz A: "))
        A = create_matrix(rows, cols)

        rows = int(input("Digite o número de colunas da matriz B: "))
        cols = int(input("Digite o número de colunas da matriz B: "))
        B = create_matrix(rows, cols)

        result = add_matrices(A, B)
        
        print("O resultado da soma é a matriz abaixo.\n")

        for inner_list in result:
            print("\n")
            for item in inner_list:
                print(str(item) + ' ', end=' ')

        print("\n")

    elif choice == 2:
        rows = int(input("Digite o número de linhas da primeira matriz: "))
        cols = int(input("Digite o número de colunas da primeira matriz: "))
        A = create_matrix(rows, cols)

        rows = int(input("Digite o número de linhas da segunda matriz: "))
        cols = int(input("Digite o número de colunas da segunda matriz: "))
        B = create_matrix(rows, cols)

        print("Digite os elementos da primeira matriz:")
        print(f"A = {format_matrix(A)}")
        print("Digite os elementos da segunda matriz:")
        print(f"B = {format_matrix(B)}")

        result = subtract_matrices(A, B)

        print("O resultado da subtração é a matriz abaixo.\n")

        for inner_list in result:
            print("\n")
            for item in inner_list:
                print(str(item) + ' ', end=' ')

        print("\n")

    elif choice == 3:
        rows = int(input("Digite o número de linhas da matriz: "))
        cols = int(input("Digite o número de colunas da matriz: "))
        A = create_matrix(rows, cols)

        result = inverse_matrix(A)

        if result.any():
            print("O resultado da inversão é a matriz abaixo.\n")
            print(result)
        else:
            print('Não é possível criar uma matriz invertida com a matriz fornecida.')

    elif choice == 4:
        rows_A = int(input("Digite o número de linhas da primeira matriz: "))
        cols_A = int(input("Digite o número de colunas da primeira matriz: "))
        rows_B = int(input("Digite o número de linhas da segunda matriz: "))
        cols_B = int(input("Digite o número de colunas da segunda matriz: "))

        if cols_A != rows_B:
            print("O número de colunas da primeira matriz deve ser igual ao número de linhas da segunda matriz.")
            continue

        A = create_matrix(rows_A, cols_A)
        B = create_matrix(rows_B, cols_B)

        print("Digite os elementos da primeira matriz:")
        print(f"A = {format_matrix(A)}")
        print("Digite os elementos da segunda matriz:")
        print(f"B = {format_matrix(B)}")

        result = multiply_matrices(A, B)
        print("O resultado é:")
        print(f"Resultado =\n{format_matrix(result)}")

    elif choice == 5:
        rows = int(input("Digite o número de linhas da matriz: "))
        cols = int(input("Digite o número de colunas da matriz: "))
        A = create_matrix(rows, cols)
        print("Digite os elementos da matriz:")
        print(f"A = {format_matrix(A)}")
        result = transpose_matrix(A)
        print("O resultado é:")
        print(f"Resultado =\n{format_matrix(result)}")

    elif choice == 6:
        rows = int(input("Digite o número de linhas da matriz: "))
        cols = int(input("Digite o número de colunas da matriz: "))
        A = create_matrix(rows, cols)
        print("Digite os elementos da matriz:")
        print(f"A = {format_matrix(A)}")
        det = determinant_matrix(A)
        print(f"O determinante é: {det}")

    elif choice == 7:
        break

    else:
        print("Opção inválida. Por favor, tente novamente.")


