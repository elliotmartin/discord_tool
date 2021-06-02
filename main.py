import scrape_boards
import discord_bot
import boards_users
import sys
if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("please provide season id")
        exit(code=1)
    print("running discord_bot.run()")
#    discord_bot.run()
    for arg in sys.argv[1:]:
        print("running scrape_boards.get_season(" + str(arg) + ")")
        scrape_boards.get_season(arg)
        print("writing...\n")
        print(boards_users.write_season(arg))

