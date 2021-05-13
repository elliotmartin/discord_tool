import scrape_boards
import discord_bot
import boards_users
import sys

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("please provide season id")
        exit(code=1)
    if not sys.argv[1]:
        exit(code=1)
    print("running discord_bot.run()")
    discord_bot.run()
    print("running scrape_boards.get_season(" + str(sys.argv[1]) + ")")
    scrape_boards.get_season(sys.argv[1])
    print("writing...\n")
    print(boards_users.write_season(sys.argv[1]))

