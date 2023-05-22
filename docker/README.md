# Dockerfile improvement explanations

## Base image and dependencies

### Problems
```
FROM ubuntu

RUN apt-get update

RUN apt-get -y install curl git gnupg
RUN curl -sL https://deb.nodesource.com/setup_12.x -O
RUN bash setup_12.x

RUN apt-get -y install nodejs
RUN apt-get install -y wget
```
- This implementation take a while to install all dependencies
- Need to build dependencies for each docker build

### Solutions
```
FROM node:12-alpine
```
- Less code
- Build faster
- No need to install dependencies as they are already in based image
- Alpine is a smaller base image than ubuntu ( ~3MB vs ~28MB ) so less dependencies installed and less attack surface for the image

## Version label
```
LABEL version="0.1"
```
Why not use the app version
```
LABEL version="1.0.0"
```

## Add multiple file
```
ADD server.js server.js
ADD index.html index.html
ADD package.json package.json
```
Can be replaced by the following
```
COPY ["server.js", "index.html", "package.json", "./"]
```

## Npm install
```
RUN npm install
```
Use prodcution option for npm install, if you have dev dependencies it will help keep the image as small as possible
```
RUN npm install --production
```

## Expose Port
```
EXPOSE 80 443
```
The app only expose the 80 port so only this one is needed
```
EXPOSE 80
```

## Image Command 
```
CMD [ "node", "server.js" ]
```
We can use ```npm start``` command created in package.json file, this way if you edit the ```node server.js``` command by adding arguments for example, it will be take in count at the next docker build without having to change the Dockerfile
```
CMD [ "npm", "start" ]
```

## Improvements that can be done
```
FROM node:18.16-alpine3.17
```
- You can set version for node version and alpine version to have more control on when to update version
- An update of the node version is recommended if it possible as the actual LTS node version is 18
- Another way to add protection to the docker is to run it rootless
```
USER node
```