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
                    matches.append(k + ' ' +  mode + ' ' + country + ' ' + data[country][mode][k])
                
    
    return matches

print(match_users('./json/73.json', './json/tags.txt'))
