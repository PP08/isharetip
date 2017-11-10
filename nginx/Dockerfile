FROM nginx
ADD uwsgi_params /app/nginx/
RUN rm /etc/nginx/conf.d/*
RUN rm /etc/nginx/nginx.conf
ADD nginx.conf /etc/nginx/

#ADD mysite_nginx.conf /etc/nginx/conf.d/