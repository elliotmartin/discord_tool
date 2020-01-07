import json
#function that reads a .json leaderboard file and a list of users and returns users that are in the leaderboard
def match_users(filename, tags):
    with open(filename, 'r') as f:
        data = json.load(f)
    with open(tags, 'r') as f:
        tags = f.readlines()
        tags = [t[0:t.find('#')].lower().strip() for t in tags]

    matches = []
    
    #woooo triple loop. new highscore! I don't think this is too horrific? 
    for country in data.keys():
        for mode in data[country].keys():
            for k in data[country][mode].keys():
                if k.lower().strip() in tags:
                #name mode country rank
                    matches.append((mode,  country,  k, str(data[country][mode][k])))
                
    
    return matches

prev_season = "74"
matched = match_users('./json/' + prev_season  + '.json', './json/tags.txt')

print("Congratulations to the following users from our server who placed on the Official Hearthstone leaderboards last month!")

print("**Standard**")
print("__US__:")
for m in matched:
    if (m[0] == "STD") and (m[1] == "US"):
        print(m[2] + " placed " + m[3])

print('\n')
print("__EU__:")
for m in matched:
    if (m[0] == "STD") and (m[1] == "EU"):
        print(m[2] + " placed " + m[3])

print('\n')
print("__APAC__:")
for m in matched:
    if (m[0] == "STD") and (m[1] == "AP"):
        print(m[2] + " placed " + m[3])

print('\n')

print("**Wild**")
print("__US__:")
for m in matched:
    if (m[0] == "WLD") and (m[1] == "US"):
        print(m[2] + " placed " + m[3])

print('\n')
print("__EU__:")
for m in matched:
    if (m[0] == "WLD") and (m[1] == "EU"):
        print(m[2] + " placed " + m[3])

print('\n')
print("__APAC__:")
for m in matched:
    if (m[0] == "WLD") and (m[1] == "AP"):
        print(m[2] + " placed " + m[3])

print('\n')

print("**Battlegrounds**")
print("__US__:")
for m in matched:
    if (m[0] == "BG") and (m[1] == "US"):
        print(m[2] + " placed " + m[3])

print('\n')
print("__EU__:")
for m in matched:
    if (m[0] == "BG") and (m[1] == "EU"):
        print(m[2] + " placed " + m[3])

print('\n')
print("__APAC__:")
for m in matched:
    if (m[0] == "BG") and (m[1] == "AP"):
        print(m[2] + " placed " + m[3])
