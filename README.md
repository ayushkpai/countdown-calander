# Countdown calander

- Open your terminal and clone this repository

  First make sure you have a ssh key if you dont have go to my dotfiles repository and follow the instructions

  ```
  git clone git@github.com:ayushkpai/countdown-calander.git
  ```

- Next install python

  Also documented in dotfiles

  Create a events.txt file

  ```
  touch events.txt
  pwd
  echo <what pwd returned/events.txt> >> .env
  ```

  In events.txt write like

  `<event>,<date>`

- To run the files

  ```
  uv run Code.py
  ```
