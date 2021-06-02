Compares users in the CompHS Discord server to the end of month Hearthstone leaderboards

discord_bot.py will automatically associate these messages with users in json/tags.json

scrape_boards.py will scrape all users from the Hearthstone leaderboards and save json data in json/SEASONID.json. This probably the most useful piece for other users to use. 

boards_users will look for users in tags.json that are in the given SEASONID

main.py does all of this sequentially and accepts any number of season parameters (eg `python3 main.py 91` or `python3 main.py 88 89 90 91`)

Usage:
git clone
python3 -m venv discord_env
source discord_env/bin/activate
pip3 install -r requirements.txt
#install phantomjs, on Mac: 
brew install phantomjs
touch .env
#edit .env to include DISCORD_TOKEN=YOUR_DISCORD_BOT_TOKEN DISCORD_GUILD=YOUR_DISCORD_GUILD_NAME
#your discord server should have a battletags channel that contains messages from users with the form of username#1111
python3 main.py SEASON_NUMBER
