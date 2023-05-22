FROM node:12-alpine

LABEL version="1.0.0"
LABEL description="A super docker image."

RUN mkdir -p /home/app 
WORKDIR /home/app

COPY ["server.js", "index.html", "package.json", "./"]
RUN wget https://www.lescinskas.lt/assets/img/posts/2019/docker.png -O background.png

RUN npm install --production

USER node

EXPOSE 80

CMD [ "npm", "start" ]