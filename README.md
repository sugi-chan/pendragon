<p align="center">
  <img width="640" height="400" src="https://cdn-images-1.medium.com/max/1200/1*OW5YsC_XyyBn6bakstvxaA.jpeg">
</p>

# Pendragon

This repository is an attempt to open source some of the work I have done around building a number of bots to play the game Fate Grand Order. The current state of this bot is that it uses the framework I built in my first bot [project pendragon](https://github.com/sugi-chan/project_pendragon) and the reinforcement learning bot that I built in my second bot [pendragon alter](https://github.com/sugi-chan/Pendragon_Alter). While the structure of this bot is relatively similar to my two previous ones, it is different in a number of ways.

## Upgrades from the previous bots

1) **Skills can now be used**: The RL bot does not have access to skills, but I have added an interface via `battle plans` with an option when running the `pendragon.py` script to feed in a formatted csv for round by round or turn by turn orders. This allows for skills and NPs to be used at specific timings and I have found useful for 3 turn farming of embers or clearing more difficult quests repeatedly

2) **Turn tracking**: I had struggled previously on how to track turns. I added a `round/wave counter` essentially made a 3 class classifier to count which round it is. downsides of this are it wouldn't detect the rare quest with a 4th wave, and isn't the most effective method for turn counting... However my logic was that most skills or NP usages that need to be scripted would need to be used on specific waves/rounds.

3) **improved a number of models**: I found that a number of models I built for my initial models did not generawlize well to different levels so I added additional examples and trained some larger models. I had been using resnet18s for detecting the attack button detection. so I retrained it and upgraded those to resnet34s. In theory the new attack button model could be used to count turns as well... but for now I think determining the round is more important.

<p align="center">
  <img width="640" height="400" src="https://cdn-images-1.medium.com/max/800/1*SfuIcXBrkxRGTWIiYIQ2dA.gif">
</p>

## Things needed to use the repo

1) To use this repo the additional model files are required download the model directory [here](https://drive.google.com/drive/folders/1JPgKi9n4vs0sEtbgji2NK5Bn5-nEcY-g?usp=sharing) and place it in this repo

2) the biggest issue right now is configuring the repo to extract game information... This is something that I am going to work on streamlining and writing more instructions for.

- `grab.py` is what I use to get a screenshot of the teamvierwer window which gets run pretty regularly. Additionally this screenshot is what gets sliced. I take a screenshot and find the screen locations of boxes that need to be cropped out like command cards, attack button, and the turn counter. Most of the inputs for this are housed in the `skill_sheet.csv`

- `mouse_pos.py`: is a helper script I use to determine the locations I need for the different sections. This is mostly for button pressing. So determining where skill buttons are,, or card where to click on a command card (previous section was how to crop them out to feed into models) or how to use master skills etc. most of these are in `utils.py`

3) My personal setup has been using pytorch 1.0.1 and tensorflow 1.0 which is now outdated. So I have not tested with the newest versions of tensorflow for breaking changes.

## TODO

- make a document or something to show to how configure the repo since there is a good bit of 1 time manual work.

- clean up code stylistically and refactor parts of it to make it cleaner. 

- add more documentation on how to do things like setup a `battle plan`.

