sudo apt update
sudo apt upgrade -y
sudo apt install virtualenv -y
virtualenv venv
source venv/bin/activate
pip install gunicorn

sudo ufw enable 6000
python3 -m web_flask.0-hello_route && gunicorn --bind 0.0.0.0:5000 web_flask.0-hello_route:app