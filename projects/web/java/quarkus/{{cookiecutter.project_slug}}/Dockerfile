FROM maven:3.9-eclipse-temurin-{{ cookiecutter._java_version }} AS build
WORKDIR /src
COPY pom.xml ./
RUN mvn -B -q dependency:go-offline
COPY src ./src
RUN mvn -B -q -DskipTests package

FROM eclipse-temurin:{{ cookiecutter._java_version }}-jre-alpine
RUN addgroup -S app && adduser -S -G app app
WORKDIR /app
COPY --from=build --chown=app:app /src/target/quarkus-app/ ./
ENV PORT=8000
EXPOSE 8000
USER app
ENTRYPOINT ["java", "-jar", "quarkus-run.jar"]
