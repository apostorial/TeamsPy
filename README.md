# Description
This is a Python3 script that checks if you have an invite link for a Teams reunion in your Outlook Educational Mail then automatically joins you to the reunion and also deactivates the mic and the camera.
# Requirements
Here are the things that you need to install before using this bot:
- Install Python3 from the official website `www.python.org`, be sure to check `Add Python to PATH` while installing it.
- Install all the requirements needed, to do that open the Command Prompt in the Bot Folder, to do that either type `cmd` in the File Explorer while you have the folder opened or open normally the Command Prompt from the search bar in Windows and type `cd (directory)`, for example if you have the bot in a folder called TeamsPy in another folder called Projects in the Desktop just type `cd Desktop/Projects/TeamsPy` then lastly run this command `pip install -r requirements` to install everything that you need.
# Data needed and how/when to run
For the correct running of the bot you will need to provide some information, here is what you need to do:
- Add your Outlook email and password in the text file called `emailpass` in this format: `email:pass`.
- Add the time when you want the bot to join the reunion in the text file called `time` in this format: `HH:MM`. It's better to do it when you're sure that you received the invitation link in the email.
- Add the hypertext that has as data the invitation link to the reunion in the text file called `invitesentence`, for example if you have in old invitation emails the following text "Click here to join the meeting" and this text leads you directly to Teams then you need to add that text. Be sure to add it without missins any characters or misspelling anything.
- In the folder called "images" you may need to change the picture "joinNow" depending on the language used in Teams, be sure to keep the same name.
Now that the bot has every data needed, you can run it, I can think of 3 ways of running it:
- Run it the night before the reunion and leave your PC on but this is too much.
- Run it minutes before the reunion and go do your usual tasks.
- Run it in a RDP (Remote Desktop Protocol) so you won't have to worry about your PC, just be extra sure about the time, because the time in a RDP can be different from yours. Just do the calculations right because the code takes the current time from the PC.
To run the bot open the cmd as explained earlier then type the following command: `py main.py` and it will display if it's waiting and what are the seconds passed and the current time while the bot is waiting for the time to match.
When the time matches, it will automatically open Chrome and start the actions, just be sure to do anything while the bot is checking because it can mess with what it does.
# DISCLAIMER
This is my first Python Project EVER, so yeah not everything is perfect.
The boy may take some time performing some actions or may do them too fast because I used the time module so the bot doesn't do something stupid even if you have a slow Internet Connection (You may need to adjust the time manually depending on your Internet and your needs). To do so just edit the `main.py` file and change the command `time.sleep()` where it lags for you if you have a slow internet or where you want it to speed up if you have a fast one. The time in that command is in seconds so if you want the bot to wait 10 seconds instead of 3 change `time.sleep(3)` to `time.sleep(10)`.
