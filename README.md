# Audio To Do List

A To Do List controlled by voice commands


## Getting Started

This version uses the command `say` from the terminal to convert text to speech.

Your to-do list is created as a .txt file so you can edit the file itself if you wish to do so.

_Note: The Audio To Do List will not work on windows._


### Prerequisites

You need the speech recognition to make the Audio To Do List work

```
pip install SpeechRecognition
```


### Installing

If you are running ubuntu you need to install the ` gnustep-gui-runtime` with the following command:


```
sudo apt-get install gnustep-gui-runtime
```

If you are running any Mac OS, you don't need to do anything.


## Commands Available

#### Quit
Say quit at any time to stop the Audio To Do List

#### Help
Say help to get quick info about all the commands available to work with the Audio To Do list

#### Create
Say create to add a new item to your to-do list

#### Listen
Say listen to listen to all the items currently in your to-do list

#### Complete
Say complete to complete an item from the to-do list

#### Delete
Say delete to delete an item from the to-do list


## Built With

* [SpeechRecognition](https://pypi.python.org/pypi/SpeechRecognition/) - Library for performing speech recognition


## Authors

* **Fabio Rosado** - *Initial work* 


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

