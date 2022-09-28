FROM node:16 as build

ARG server_ip
ENV IP=${server_ip}

COPY . /.
RUN npm install
RUN echo "VITE_SERVER_IP=$IP" > .env
RUN npm run build


FROM nginx:stable

ARG server_ip
ENV IP=${server_ip}

RUN mkdir /www
COPY --from=build dist/ /www
COPY --from=build nginx.conf /etc/nginx/nginx.conf
RUN sed -i "s/server_name x.x.x.x;/server_name ${IP};/" /etc/nginx/nginx.conf
