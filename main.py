from fastapi import FastAPI
import ipl

app = FastAPI()

@app.get('/')
def home():
    return "Welcome to the IPL teams API"

@app.get('/api/teams')
def teams():
    teams_list = ipl.TeamsAPI()
    return teams_list

@app.get('/api/team_headon/{team_1}/{team_2}')
def team_fight(team_1: str, team_2: str):
    results = ipl.team_vs_team(team_1, team_2)
    return results