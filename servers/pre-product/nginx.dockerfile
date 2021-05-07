FROM nginx:1.20.0

RUN apt-get update && apt-get install vim wget -y
COPY servers/intermediate_server/nginx/sites-available/homebooks.conf /etc/nginx/sites-available/
# RUN mkdir /etc/nginx/sites-available/sites-enabled/
# RUN ln -s /etc/nginx/sites-available/homebooks.conf /etc/nginx/sites-enabled/
COPY servers/intermediate_server/nginx/index.html /usr/share/nginx/html/index.html
