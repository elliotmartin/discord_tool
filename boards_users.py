import json
#function that reads a .json leaderboard file and a list of users and returns users that are in the leaderboard
def match_users(filename, tags):
    with open(filename, 'r') as f:
        data = json.load(f)
    with open(tags, 'r') as f:
        tags = f.readlines()
        tags = [t[0:t.find('#')].lower().strip() for t in tags]

    print(tags) 
    matches = []
    
    #this needs a lot of work done
    for country in data.keys():
        for mode in data[country].keys():
            if str(data[country][mode]).lower().strip() in tags:
                #name mode country rank
                matches.append(data[country][mode] + ' ' +  mode + ' ' + country + ' ' + data[data[country][mode]])
                
    
    return matches

print(match_users('./json/73.json', './json/tags.txt'))
