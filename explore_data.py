from pybaseball import statcast

# Pull every pitch-level Statcast event recorded in the given date range
data = statcast(
    start_dt="2026-08-01",
    end_dt="2026-08-03",
)

# Keep only pitches from games the Braves played in (home or away)
braves_games = data[
    (data["home_team"] == "ATL") |
    (data["away_team"] == "ATL")
]

# Narrow down to pitches where the Braves were batting:
# either they're the home team batting in the bottom of the inning,
# or they're the away team batting in the top of the inning
braves_hitting = braves_games[
    ((braves_games["home_team"] == "ATL") &
     (braves_games["inning_topbot"] == "Bot"))
    |
    ((braves_games["away_team"] == "ATL") &
     (braves_games["inning_topbot"] == "Top"))
]

# Report how many pitches the Braves saw at the plate
print("Braves hitting pitches:", braves_hitting.shape)