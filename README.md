# pymentionbot
A simple Python script that mentions with an image an user that mentions another user(in the most common case, the bot itself)

# Usage
1. Put your Twitter tokens in auth.py file, one in each variable.
2. In bot.py, change MY_TWITTER_NAME to your Twitter username, including the @ at the start of it.
3. Run bot via console by typing "python bot.py"

# Additional info
You can change the input image by replacing the img.jpg for a new one.
The text gets a new line every 3 words, but you can adjust it in bot.py by changing the logic of the for loops in lines 27 and 31.
