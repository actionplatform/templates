FROM node:20-alpine AS build
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

FROM nginx:1.27-alpine
COPY --from=build /app/build /usr/share/nginx/html
EXPOSE 8000
RUN sed -i 's/listen       80;/listen       8000;/' /etc/nginx/conf.d/default.conf
