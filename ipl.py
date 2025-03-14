import pandas as pd

# Read the dataset
ipl_matches = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRy2DUdUbaKx_Co9F0FSnIlyS-8kp4aKv_I0-qzNeghiZHAI_hw94gKG22XTxNJHMFnFVKsO4xWOdIs/pub?gid=1655759976&single=true&output=csv"
matches = pd.read_csv(ipl_matches)

def TeamsAPI():
    # Directly use set and then convert to list to get unique teams
    teams_participated = list(set(matches['Team1']).union(set(matches['Team2'])))
    
    return {
        "teams": teams_participated
    }

def team_vs_team(team1: str, team2: str):

    valid_teams = list(set(matches['Team1']).union(set(matches['Team2'])))

    if ((team1 in valid_teams) and (team2 in valid_teams)):
        # Filter the DataFrame only once
        head_on_df = matches[((matches['Team1'] == team1) & (matches['Team2'] == team2)) |
                            ((matches['Team2'] == team1) & (matches['Team1'] == team2))]
        
        # Calculate wins and no results in a more efficient way
        winning_counts = head_on_df['WinningTeam'].value_counts()
        team1_win = int(winning_counts.get(team1, 0))
        team2_win = int(winning_counts.get(team2, 0))
        no_res = int(head_on_df.shape[0] - (team1_win + team2_win))
        
        return {
            "Total matches": head_on_df.shape[0],
            team1: team1_win,
            team2: team2_win,
            "No results": no_res
        }
    else:
        return {
            "message" : "Invalid Team Name"
        }