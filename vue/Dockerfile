FROM node:16

COPY . /.
RUN npm install

EXPOSE 5173
ENTRYPOINT npm run dev -- --host
