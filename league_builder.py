# Import library

import csv

# Make program not run when imported

if __name__ == '__main__':


# Player lists (experienced players and non)

	exp_player = []
	non_exp = []

# Make CSV into Dict then seperate by experience


	with open('soccer_players.csv') as csvfile:
		playerreader = csv.DictReader(csvfile, delimiter=',')
		rows = list(playerreader)
		for row in rows:
			if row['Soccer Experience'] == "YES":
				exp_player.append(row)
			else:
				non_exp.append(row)

# Combine nonexperienced players and experienced players into teams
	exp_1 = exp_player[::3]
	exp_2 = exp_player[1::3]
	exp_3 = exp_player[2::3]
	non_exp_1 = non_exp[::3]
	non_exp_2 = non_exp[1::3]
	non_exp_3 = non_exp[2::3]
	sharks = exp_1 + non_exp_1
	dragons = exp_2 + non_exp_2
	raptors = exp_3 + non_exp_3
	

# Write teams.txt files

	with open('teams.txt', 'a') as file:
		file.write('Sharks\n')
		for player in sharks:
			file.write('{Name}, {Soccer Experience}, ' '{Guardian Name(s)}\n'.format(**player))
		file.write('\nDragons\n')
		for player in dragons:
			file.write('{Name}, {Soccer Experience}, ' '{Guardian Name(s)}\n'.format(**player))
		file.write('\nRaptors\n')
		for player in raptors:
			file.write('{Name}, {Soccer Experience}, ' '{Guardian Name(s)}\n'.format(**player))