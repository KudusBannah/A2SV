from collections import defaultdict

def adjacency_matrix_to_adjacency_list(adj_matrix):
    adj_list = defaultdict(list)
    for i in range(len(adj_matrix)):
        for j in range(len(adj_matrix[i])):
            if adj_matrix[i][j]:
                adj_list[i].append(j)

    return adj_list


def adjacency_list_to_matrix(adj_list):
    adj_matrix = []
    for i in range(len(adj_list)):
        new_matrix = [0 for i in range(len(adj_list))]
        adj_matrix.append(new_matrix)
    
    for el in adj_list:
        for neighbour in adj_list[el]:
            adj_matrix[el][neighbour] = 1

    print(adj_matrix)

    return adj_matrix


def edge_list_to_adjacency_list(edge_list):
    adj_list = defaultdict(list)
    for edge in edge_list:
        adj_list[edge[0]].append(edge[1])

    return adj_list
