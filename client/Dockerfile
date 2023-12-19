FROM node:18-alpine as base
WORKDIR /usr/src/app/

COPY package*.json ./

FROM base as builder
WORKDIR /usr/src/app/

COPY . .

RUN npm run build

FROM base as production
WORKDIR /usr/src/app/

ENV NODE_ENV=production
RUN npm ci

COPY --from=builder --chown=nextjs:nodejs /usr/src/app/.next ./.next
COPY --from=builder /usr/src/app/node_modules ./node_modules
COPY --from=builder /usr/src/app/package.json ./package.json
COPY --from=builder /usr/src/app/public ./public

CMD npm start

FROM base as dev
ENV NODE_ENV=development
RUN npm ci 
COPY . .
CMD npm run dev