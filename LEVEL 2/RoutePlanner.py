# route_exists: quick filter if the destination is reachable, before using more computationally intensive procedures 
#               for finding the optimal route.
#    -> returns True if the destination is reachable or False if it is not.
#    -> from_row and from_column parameters are the starting row and column in the map_matrix.
#    -> to_row and to_column are the destination row and column in the map_matrix.
#    -> map_matrix parameter is the above mentioned matrix produced from the map.

# The roads on the map are rasterized and produce a matrix of boolean values True if the road is present or False if it is not.
#    - roads in the matrix are connected only if the road is immediately left, right, below or above it.

# from collections import deque

# def route_exists(from_row, from_column, to_row, to_column, map_matrix):
#     dx = [-1,1,0,0]
#     dy = [0,0,-1,1]
#     queue = deque()
#     queue.append((from_row, from_column))
    
#     while queue:
#       from_row, from_column = queue.popleft()
#       for i in range(4):
#         nx = from_row + dx[i]
#         ny = from_column + dy[i]
        
#         if nx < 0 or nx >= to_row or ny < 0 or ny >= to_column:
#           continue
#         if map_matrix[nx][ny] == False:
#           continue
#         if map_matrix[nx][ny] == True:
# #           map_matrix[nx][ny] = map_matrix[from_row][from_column] + 1
#            queue.append((nx,ny))


class RoutePlanner:
  """
  Class RoutePlanner created to try to pass through a matrix from one index to another.
  """

  def __init__(self, matrix:list, to_row:int=0, to_column:int=0):
    """
    Args:
      matrix (list): A matrix used to be analyzed.
      to_row (int, optional): A end row index of the path. Default 0.
      to_column (int, optional): A end column index of the path. Default 0.
    """
    self.to_row = to_row
    self.to_column = to_column
    self.matrix = matrix
    self.visited = [[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]


  def valid_move(self, row:int, column:int) -> bool:
    """
    Checks if the row and column index in the array is a valid index.
    Args:
      row (int): Row index of the matrix.
      column (int): Column index of the matrix.
    Returns:
      (bool): A boolean returns used to return if a position in matrix is valid.
    """
    if row >= 0 and column >= 0 and row < len(self.matrix) and column < len(self.matrix[0]):
      if self.matrix[row][column] and not self.visited[row][column]:
        return True

    return False


  def find_path(self, row:int, column:int) -> bool:
    """
    Try to find a path from one index to another.
    Args:
      row (int): Row index of the matrix.
      column (int): Column index of the matrix.
    Returns:
      (bool): A boolean returns if there is a path to certain positions in the matrix.
    """
    if not self.valid_move(row, column): return False
    
    if row == self.to_row and column == self.to_column: return True
    
    self.visited[row][column] = True

    return (self.find_path(row - 1, column) or
            self.find_path(row, column - 1) or
            self.find_path(row + 1, column) or
            self.find_path(row, column + 1))


def route_exists(from_row:int, from_column:int, to_row:int, to_column:int, matrix:list) -> bool:
  """
  Try to pass through a matrix from one index to another and returns if there is a path to the destination.
  Args:
    from_row (int): A start row index of the path.
    from_column (int): A start column index of the path.
    to_row (int): A end row index of the path.
    to_column (int): A end column index of the path.
    matrix (list): A matrix used to be analyzed.
  Returns:
    path (bool): A boolean variable used to return if a path to the destination exists.
  """
  if type(from_row) != int or type(from_column) != int or type(to_row) != int or type(to_column) != int: raise Exception("The indexes must be integers!")
  if type(matrix) != list: raise TypeError("The matrix must be a list!")
  try:
    if not matrix[from_row][from_column] or not matrix[to_row][to_column]: return False
  except IndexError:
    raise IndexError("The indexes must be valid indexes!")

  route_planner = RoutePlanner(matrix, to_row, to_column)
  return route_planner.find_path(from_row, from_column)


if __name__ == "__main__":

  map_matrix = [[True, False, False],
                [True, True, False],
                [False, True, True]]
  
  print(route_exists(0, 0, 2, 2, map_matrix))

if __name__ == '__main__':
    map_matrix = [
        [True, False, False],
        [True, True, False],
        [False, True, True]
    ];

    print(route_exists(0, 0, 2, 2, map_matrix))
