


def write_players_ids(perm_team):

    for player in perm_team.player_list:
        side=player.side
        height=player.height
        player.id= perm_team.q_pos[side][height]

def change_players_side(perm_team):

    perm_team.q_pos = invert_matrix(perm_team.q_pos)

def invert_matrix(matrix):
    if len(matrix) != len(matrix[0]):
        raise ValueError("¡La matriz debe ser cuadrada!")
    
    n = len(matrix)
    invertida = [[0] * n for _ in range(n)]  # Crear una matriz vacía con las mismas dimensiones
    
    for i in range(n):
        for j in range(n):
            if i == j:
                # Intercambiar elementos diagonales
                invertida[i][j] = matrix[n - i - 1][n - j - 1]
            else:
                # Mantener elementos fuera de la diagonal
                invertida[i][j] = matrix[j][i]
    
    return invertida

