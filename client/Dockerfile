FROM node:18-alpine as base
WORKDIR /usr/src/app/

COPY package*.json ./

FROM base as builder
WORKDIR /usr/src/app/

COPY . .

RUN npm run build

FROM base as dev
ENV NODE_ENV=development
RUN npm ci 
COPY . .
CMD npm run dev