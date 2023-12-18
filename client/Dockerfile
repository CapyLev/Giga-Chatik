FROM node:18-alpine as base
WORKDIR /app

COPY package*.json ./

FROM base as builder
WORKDIR /app

COPY . .

RUN npm run build

FROM base as production
WORKDIR /app

ENV NODE_ENV=production
RUN npm ci

COPY --from=builder --chown=nextjs:nodejs /app/.next ./.next
COPY --from=builder /app/node_modules ./node_modules
COPY --from=builder /app/package.json ./package.json
COPY --from=builder /app/public ./public

CMD npm start

FROM base as dev
ENV NODE_ENV=development
RUN npm ci 
COPY . .
CMD npm run dev