# <img src="https://www.shareicon.net/download/2016/11/16/854126_color.ico" height="40px"> Insta-Clone 

InstaClone is a app where users can post pics, comment, like and follow their friends.

## Application
<img src="/static/mypics/Screenshot from 2018-10-09 17-25-51.png">

## User stories

The user should be able to:

+ [x] Sign in to the application to start using.
+ [x] Upload my pictures to the application.
+ [x] See my profile with all my pictures.
+ [x] Follow other users and see their pictures on my timeline.
+ [x] Like a picture and leave a comment on it.

## Prerequisites
+ [x] Python3.6

## Installation
To install, follow the following instructions;

```bash
    $ git clone https://github.com/MutumaMutuma/Insta-Clone.git
    $ cd Insta-Clone
    $ source virtual/bin/activate
    Install all the necessary requirements by running pip install -r requirements.txt (Python 3.6).
    $ ./manager.py runserver
```
## How to Prepare enviroment variables
Since one needs a virtual enviroment, Create a virtual file and add the following configutions to it

```bash
    SECRET_KEY= #secret key will be added by default
    DEBUG= #set to false in production
    DB_NAME= #database name
    DB_USER= #database user
    DB_PASSWORD=#database password
    DB_HOST="127.0.0.1"
    MODE= # dev or prod , set to prod during production
    ALLOWED_HOSTS='.localhost', '.herokuapp.com', '.127.0.0.1'
```
## Insta-Clone Demo

This is the live link to Insta-clone [Click here](https://luwigram.herokuapp.com)

## Technology used

* [Python3.6](https://www.python.org/)
* [Django 1.11](https://www.djangoproject.com/)
* [Heroku](https://heroku.com)
* [Bootstrap](https://www.getbootstrap.com/)

## License ([MIT License](https://github.com/MutumaMutuma/Insta-clone/blob/master/LICENSE))
This project is licensed under the MIT Open Source license, (c) [Lewis Mutuma](https://github.com/MutumaMutuma)