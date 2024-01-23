
def parse_card_details(line):
    parts = line.split(":")
    card_id = parts[0].strip().split()[1]
    numbers = parts[1].split("|")
    winning_numbers = {int(num) for num in numbers[0].split()}
    my_numbers = {int(num) for num in numbers[1].split()}
    return card_id, winning_numbers, my_numbers


def calculate_wins(line):
    card_id, winning_numbers, my_numbers = parse_card_details(line)
    matched_numbers = winning_numbers.intersection(my_numbers)
    return len(matched_numbers)

def calculate_points(all_games):
  num_cards = [1] * (len(all_games))
  for i, g in enumerate(all_games):
    for j in range(i+1, i+g+1):
      num_cards[j] += num_cards[i]
  return num_cards    

  
with open('input', 'r') as fp:
  ag= [calculate_wins(l) for l in fp.readlines()]

print(sum(calculate_points(ag)))
