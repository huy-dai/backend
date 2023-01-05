# Template React + Flask framework

Created and maintained by: TheReddKing (TechX)

## Dev:

### Local Installation:

I found that the installation requires Python v3.9, since some of the older packages seem to break with newer Python v3.10 or later:

To install Python v3.9 in Ubuntu you can do:

    sudo apt install software-properties-common
    sudo add-apt-repository ppa:deadsnakes/ppa
    sudo apt update
    sudo apt install python3.9
    sudo apt install python3.9-distutils

Assuming Python v3.9 is installed at `usr/bin/python3.9`, you can do:

    virtualenv -p /usr/bin/python3.9 env
    source env/bin/activate
    pip3 install --upgrade pip
    pip3 install -r requirements.txt
    yarn
    cp .env.example .env
    cd client && yarn

Then edit your `.env` file. Once your database url is correct (you can use `createdb template` if you have postgres)

    python manage.py db init
    python manage.py db migrate
    python manage.py db upgrade

### Dev run

    yarn run dev
    
or (if you want to debug server side scripts)

    yarn start
    yarn run dev-server


### Editing

Look at the HOWTHISWASMADE.md file for more information

## Deploy on HEROKU

You first need to actually create a heroku application. You can also use the `app.json` to deploy (you can read about it somewhere else)

Then you need to copy over the environmental variables from your local computer

    sed 's/#[^("|'')]*$//;s/^#.*$//' .env | \
    xargs heroku config:set

Afterwards, a simple heroku push will configure everything

    git push heroku master
