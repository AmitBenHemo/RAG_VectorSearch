FROM node:18-alpine

WORKDIR /app

COPY package.json .
COPY .env .

RUN npm install

RUN npm i -g serve

COPY . .

RUN npm run build

ENV VITE_API_BASE_URL=http://127.0.0.1:8000

EXPOSE 3000

CMD [ "serve", "-s", "dist" ]