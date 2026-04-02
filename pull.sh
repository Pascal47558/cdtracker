if $1="1"; then
    cd ~/cdtracker
else
    cd /home/rowan/cdtracker
fi

git pull

python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py collectstatic --noinput

sudo systemctl restart gunicorn
