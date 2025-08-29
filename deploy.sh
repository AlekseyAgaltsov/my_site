#!/bin/bash
sudo apt update & sudo apt upgrade –y
sudo apt install git
sudo git clone https://github.com/AlekseyAgaltsov/my_site.git
sudo apt update
sudo apt install python3-venv python3-dev libpq-dev  nginx curl python-3-pip -y
sudo chmod -R 755 my_site/
cd my_site/
#sudo python3 -m venv myprojectenv
#source myprojectenv/bin/activate
sudo apt install python3-django python3-gunicorn python3-psycopg2-binary
#pip install django gunicorn psycopg2-binary

sudo apt install python3-pandas
python3 manage.py runserver <local_ip:port>

# https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-18-04-ru
# Для загрузки статики предоставить права
sudo chmod o+x /home/agaltsovaa

# Проверка gunicorn
Gunicorn --bind 0.0.0.0:8000 ntdl.wsgi

Создаем файл сокета /etc/systemd/system/gunicorn.socket
[Unit]
Description=gunicorn socket
[Socket]
ListenStream=/run/gunicorn.sock
[Install]
WantedBy=sockets.target

Теперь создайте и откройте служебный файл systemd для Gunicorn
[Unit]
Description=gunicorn daemon
Requires=gunicorn.socket
After=network.target
[Service]
User=agaltsovaa
Group=www-data
WorkingDirectory=/home/agaltsovaa/my_site
Environment=’’PATH=/usr/local/bin’’
ExecStart=/usr/bin/gunicorn \
          --access-logfile - \
          --workers 3 \
          --bind unix:/run/gunicorn.sock \
          ntdl.wsgi:application
[Install]
WantedBy=multi-user.target
Настройка Nginx как прокси для Gunicorn
$ sudo nano /etc/nginx/sites-available/my_site
server {
    listen 80;
    server_name 192.168.88.30;
    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /home/agaltsovaa/my_site;
    }
    location / {
        include proxy_params;
        proxy_pass http://unix:/run/gunicorn.sock;
    }
}
Сохраните файл и закройте его после завершения. Теперь мы можем активировать файл, привязав его к каталогу sites-enabled:
sudo ln -s /etc/nginx/sites-available/my_site /etc/nginx/sites-enabled

Протестируйте конфигурацию Nginx на ошибки синтаксиса:
sudo nginx -t
Если ошибок не будет найдено, перезапустите Nginx с помощью следующей команды:
sudo systemctl restart nginx

$ sudo nano /etc/nginx/sites-enable/default прописал те же настройки
