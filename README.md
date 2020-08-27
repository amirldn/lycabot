# lycabot
New &amp; Improved version of the original lycasimbot


## Getting Started
**Instructions**

1 ) Clone the repository

2 ) Install dependencies

    pip install -r requirements.txt

2 ) Install chromedriver for your OS
- For MacOS, use brew and execute
    
        brew cask install chromedriver

3 ) Run the code
       
       python3 simOrder.py
       
4 ) Enjoy your free sim cards!

**To-do**
- ~~Add an option to allow for multiple sim cards in one order~~ DONE
- Add an option to allow more than 3 SIMs to be ordered in one run of the script
- ~~Add captcha-bypass prevention (fails the bot 50% of the time as of right now)~~ DONE
- Add ability to manually enter address for users living in flats or uncommon addresses etc.
- Proxy Support

**Known Issues**
- Does not natively work with Windows PC due to a line of code. Current work around is change the line 

         with open('./data/names.txt') as file_with_names:
         into 
         with open(' <DIRECTORY OF THE GIT DIR YOU CLONED>/data/names.txt') as file_with_names:
