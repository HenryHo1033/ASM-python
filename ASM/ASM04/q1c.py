import csv
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
filename = os.path.join(dir_path, "NBAStat.csv")

try:
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header line
        teams = []
        for row in reader:
            team = {
                'name': row[0],
                'play': int(row[1]),
                'win': int(row[2]),
                'draw': int(row[3]),
                'lose': int(row[4]),
                'for': int(row[5]),
                'against': int(row[6]),
                'diff': int(row[7]),
                'points': int(row[8])
            }
            teams.append(team)

        # Find the top 5 teams with the highest points
        top_five = sorted(teams, key=lambda x: x['points'], reverse=True)[:5]
        print("Top 5 teams with the highest points:")
        for team in top_five:
            print(f"{team['name']}: {team['points']} points")

        # Find the number of teams with name containing "Angeles" and won fewer than 1000 games
        angeles_teams = [team for team in teams if "Angeles" in team['name'] and team['win'] < 1000]
        num_angeles_teams = len(angeles_teams)
        print(f"Number of teams with name containing 'Angeles' and won fewer than 1000 games: {num_angeles_teams}")

        # Find the number of teams that have played over 2000 games and scored over 5000
        scored_over_5000 = [team for team in teams if team['for'] > 5000 and team['play'] > 2000]
        num_scored_over_5000 = len(scored_over_5000)
        print(f"Number of teams that have played over 2000 games and scored over 5000: {num_scored_over_5000}")

except FileNotFoundError:
    print(f"Error: NBAStat.csv not found.")
except IOError:
    print("Error reading file.")