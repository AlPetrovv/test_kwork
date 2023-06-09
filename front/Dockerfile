FROM node:15.5.1 as build


WORKDIR .

COPY . .
RUN npm install express
CMD [ "node", "index.js" ]