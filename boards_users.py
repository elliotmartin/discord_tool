import json
#function that reads a .json leaderboard file and a list of users and returns users that are in the leaderboard
def match_users(filename, tags):
    with open(filename, 'r') as f:
        data = json.load(f)
        #print(data)
    with open(tags, 'r') as f:
        tags = json.load(f)
        #print(tags)
        just_tags = [t[0:t.find('#')].lower().strip() for t in tags.keys()]
#the tags list needs to be declared as a seperate variable so that we can still index the JSON tags to find discord users from battletags, other variables need to be updated appropriately
    matches = []
    
    #woooo triple loop. new highscore! I don't think this is too horrific? 
    for country in data.keys():
        #print(country)
        for mode in data[country].keys():
            #print(mode)
            for k in data[country][mode].keys():
                if k.lower().strip() in just_tags:
                #name mode country rank
                    player_name = str(data[country][mode][k])
                    #print('name: ' + player_name)
                    #print(mode, country, k , player_name)
                    matches.append((mode,  country,  k, player_name)) #tags[k]))
                
    
    return matches

def write_season(prev_season):
    matched = match_users('./json/' + str(prev_season)  + '.json', './json/tags.json')
    result=""
    result += "Congratulations to the following users from our server who placed on the Official Hearthstone leaderboards last month!\n"


    for mode in ['STD', 'WLD', 'CLS', 'BG']:
        result += '**' + mode + '**\n'
        for region in ['US', 'EU', 'AP']:
            result += '__' + region + '__\n'
            for m in matched:
                if (m[0] == mode) and (m[1] == region):
                    result += m[2] + " placed " + m[3] + "\n"
    return result
