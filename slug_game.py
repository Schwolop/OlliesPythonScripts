import operator
import random

colours = ['red', 'green', 'blue', 'orange', 'yellow']
road_length = 20
operators = {'-': operator.sub,
			 '+': operator.add}

def char_replace(string, index, char):
	return string[:index] + char + string[index+1:]

def draw_road(road_length, player_state):
	"""
	Draws the road.
	"""
	print('-'*road_length)
	for p in player_state:
		slug_icon = 'S'
		pos = p['pos']
		road_lane = '%s%s%s (%s the %s slug)' % (' '*pos, slug_icon, 
			' '*(road_length-pos), 
			p['name'], p['colour'])
		if pos != road_length:  # Draw the finish line unless the player is on it.
			road_lane = char_replace(road_lane, road_length, '|')
		print(road_lane)
		print('-'*road_length)

def run_round(player_state):
	op = random.choice(list(operators.keys()))  # Pick a random operator
	for p in player_state:
		operand1 = random.randrange(1,9)
		operand2 = random.randrange(1,9)
		operand_left = max(operand1, operand2)  # Ensure left operand is the greater number
		operand_right = min(operand1, operand2)
		question = '%d %s %d' % (operand_left, op, operand_right)
		answer = operators[op](operand_left, operand_right)
		players_answer_raw = input("Ok %s, what is %s? " % (p['name'], question))
		try:
			players_answer = int(players_answer_raw)
		except ValueError:
			print("That's not a number! No move for you!")
		if players_answer == answer:
			moves = random.randrange(2,4)
			print("Correct! You move %d spaces" % (moves, ))
			p['pos'] += moves
		else:
			print("Sorry, that's not right.")

		# Clamp players at road length.
		p['pos'] = min(p['pos'], road_length)

	# Draw the road.
	draw_road(road_length, player_state)
	
	return player_state

def main():
	print("Welcome to the Slug Game!")
	_in = input("Tell me who is playing:\r\n")
	players = [a.strip() for a in _in.split(',')]
	print("Looks like %d players: %s" % (len(players), players))
	
	# Create list of player states
	player_state = []
	for i, p in enumerate(players):
		player_state.append({'name': p, 'pos': 0, 'colour': colours[i]})

	# Until done, run each round and then redraw the game state.
	while True:
		player_state = run_round(player_state)

		# Check if anyone finished, and if so, who.
		finishers = []
		for p in player_state:
			if p['pos']==road_length:
				finishers.append(p['name'])
		if finishers:
			if len(finishers) == 1:
				print("The winner is %s!" % finishers[0])
			else:
				print("It's a tie between %s" % ' and '.join(finishers))
			break

if __name__ == '__main__':
	main()
