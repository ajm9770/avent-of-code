with open('input', 'r') as f:
  txt = [list(k.strip()) for k in f.readlines()]

with open('input', 'r') as f:
  print(
      set(f.read()) - {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.'})


def find_numbers(grid):
  numbers = []
  for i in range(len(grid)):
    j = 0
    while j < len(grid[i]):
      if not grid[i][j].isdigit():
        j += 1
      else:
        p = j
        while j < len(grid[i]) and grid[i][j].isdigit():
          j += 1
        numbers.append((int(''.join(grid[i][p:j])), i, p, j))
  return numbers


def filter_adjacent_numbers(grid, numbers):
  adj_chars = {'=', '@', '$', '+', '%', '#', '*', '&', '/', '-'}
  filtered_numbers = []
  for num in numbers:
    num, i, j, k = num
    for di in range(-1, 2):
      for dj in range(j - 1, min(len(grid[i]), k + 1)):
        if 0 <= i + di < len(grid) and 0 <= dj < len(
            grid[i]) and grid[i + di][dj] in adj_chars:
          filtered_numbers.append(num)
          break
  return filtered_numbers


def find_gears(grid, gears_info):
  gears = []
  for gear in gears_info:
    x, y = gear
    adjacent_nums = [
        int(grid[x - 1][y - 1]),
        int(grid[x - 1][y + 1]),
        int(grid[x + 1][y - 1]),
        int(grid[x + 1][y + 1])
    ]
    if sum(1 for num in adjacent_nums if num != '*' and num.isdigit()) == 2:
      gear_ratio = int(grid[x - 1][y - 1]) * int(grid[x - 1][y + 1])
      gears.append(gear_ratio)
  return sum(gears)


def find_gears_loc(grid):
  gears = []
  for i in range(len(grid)):
    for j in range(len(grid[i])):
      if grid[i][j] == '*':
        gears.append((i, j))
  return gears

def find_adjacent_gears_numbers(grid):
    gear_locations =  find_gears_loc(grid)
    numbers = find_numbers(grid)
    result = {}
    out_result = []
    for gear in gear_locations:
        x, y = gear
        for num in numbers:
            number, i, j, k = num
            if x-1 <= i <= x+1 and (y-1 <= j <= y+1 or y <= k <= y+2):
                if gear not in result:
                    result[gear] = []
                result[gear].append(num)
    for gear, nums in result.items():
        if len(nums) == 2:
          n1 = nums[0][0]
          n2 = nums[1][0]
          out_result.append(n1 * n2)
    return sum(out_result)

print(find_adjacent_gears_numbers(txt))

