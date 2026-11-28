FROM node:{{ cookiecutter._node_version }}-alpine AS deps
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm ci --omit=dev

FROM deps AS build
RUN npm ci
COPY .code_quality/tsconfig.json .code_quality/tsconfig.json
COPY src src
RUN npm run build

FROM node:{{ cookiecutter._node_version }}-alpine
WORKDIR /app
ENV NODE_ENV=production PORT=8000
COPY --from=deps /app/node_modules node_modules
COPY --from=build /app/dist dist
COPY package.json ./
USER node
EXPOSE 8000
HEALTHCHECK --interval=30s --timeout=3s --start-period=10s CMD node -e "fetch('http://127.0.0.1:'+process.env.PORT+'/health').then(r=>process.exit(r.ok?0:1),()=>process.exit(1))"
CMD ["node", "dist/server.js"]
