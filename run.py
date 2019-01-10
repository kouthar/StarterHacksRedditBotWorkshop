import praw
import bot

#getting the list of comments id's replied to
comments_replied = bot.get_comments_replied()

#logs in and authenticates your bot
#login is in the bot.py file
login = bot.authenticate()

#runs forever so long as you are running
#your script
while True:
	bot.run(login, comments_replied)

	