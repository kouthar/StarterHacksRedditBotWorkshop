import praw
import config
import time
import os

def authenticate():
	#bot's info
	login = praw.Reddit(username = config.username, 
		password = config.password, 
		client_id = config.client_id, 
		client_secret = config.client_secret, 
		user_agent = config.user_agent)
	return login

login = authenticate()


def get_comments_replied():
	#checks if the file exists 
	if not os.path.isfile("comments_replied.txt"):
		comments_replied = []
	else:
	# file reader - with name of file and "r" which means
	#we'll be reading the file
		with open("comments_replied.txt", "r") as file:
			#creates list of comment id's (each line)
			comments_replied = file.read()
			#putting comment id's into comments_replied.txt
			comments_replied = comments_replied.split("\n")
			#filters out empty lines from the list
			comments_replied = filter(None, comments_replied)

	#returns the list of comment id's
	return comments_replied

comments_replied = get_comments_replied()


def run(login, comments_replied):

	#looking in first 25 comments of r/test
	#limit of 25 "actions" per second
	for comment in login.subreddit('test').comments(limit=25):
		#checks if given string is in a comment's body and that 
		#the ID of the comment isn't already in comments_replied.txt
		if "this text is" in comment.body and comment.id not in comments_replied:
			
			#replying to comment
			print("Found applicable comment")

			comment.reply("This is just a demo!")

			print("Replied to applicable comment")

			#adds comment id to comments_replied list
			comments_replied.append(comment.id)

			#adds comment id to comments_replied.txt
			#for long term storage
			with open("comments_replied.txt", "a") as file:
				file.write(comment.id + "\n")

	#1min delay due to limits
	time.sleep(60)
