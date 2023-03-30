# Sweater

I was wearing a sweater when I was thinking about having my own blog, so I'v got the idea to name it Sweater; it has nothing to do with Twitter ;)

I am not a front-end developer, this is the best I could do.

# Setup and run
To run Sweater in development mode:

- Install `git` and `python3`

- Clone and cd to the project:
```bash
git clone https://github.com/MortezaShoeibi/Sweater.git && cd Sweater/
```
- Create and activate a virtual environment: 
```bash
python3 -m venv env
# then:
source env/bin/activate
```
- On windows:
```powershell
python -m venv env
# then:
./env/Scripts/activate
```
- Install required packages:
```bash
pip3 install -r requirements.txt
```
- Create database tables:
```bash
python3 ./manage.py migrate
```
- run:
```bash
python3 ./manage.py runserver
```
Your version of Sweater will be running on this address: `127.0.0.1:8000` add it to your browser search path and you will be able to see your own Sweater running locally.

To add content to your Sweater you need to get into the admin panel, for this follow these steps below:
- Create a super user:
```bash
python3 ./manage.py createsuperuser
```
- Login to this address `127.0.0.1:8000/admin` using the user you created before and add your content

# LICENSE

This is a free software published under the MIT LICENSE, feel free to copy, modify, change or do whatever you want. check the [LICENSE](./LICENSE) file for more information.

# TODO:
* [ ] fix the 'heart disappearing after unliking' bug
* [ ] launch the project
