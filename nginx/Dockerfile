FROM nginx
ADD uwsgi_params /app/nginx/
RUN rm /etc/nginx/conf.d/*
ADD mysite_nginx.conf /etc/nginx/conf.d/