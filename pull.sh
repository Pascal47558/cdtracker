cd /home/chipbort/cdtracker

git pull

python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py collectstatic --noinput

sudo systemctl restart gunicorn
