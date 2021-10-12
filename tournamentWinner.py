def tournamentWinner(competitions, results):
	points = {}
	# Iterate through each competition
    for i, pair in enumerate(competitions):
		# home team won
		if results[i] == 1:
			winner = pair[0]
			looser = pair[1]
		# away team won
		else:
			winner = pair[1]
			looser = pair[0]
		# add winner to dictionary
		if winner in points.keys():
			points[winner] += 3
		else:
			points[winner] = 3
		# add looser to dictionary
		if looser in points.keys():
			points[looser] += 0
		else:
			points[looser] = 0
	winner = None
	winningScore = 0
	for key in points.keys():
		if points[key] > winningScore:
			winner = key
			winningScore = points[key]
	return winner
		
		
