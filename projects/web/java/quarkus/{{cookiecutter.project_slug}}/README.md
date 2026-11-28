# {{ cookiecutter.project_name }}

{% if cookiecutter.description %}{{ cookiecutter.description }}

{% endif %}## Run

```bash
mvn -B quarkus:dev             # http://localhost:8000/health, live reload
java -jar target/quarkus-app/quarkus-run.jar   # after mvn -B package
```

`PORT` overrides the listen port (default `8000`) through `quarkus.http.port=${PORT:8000}`.

## Docker

```bash
docker build -t {{ cookiecutter.project_slug }} .
docker run --rm -p 8000:8000 {{ cookiecutter.project_slug }}
```

The image runs `quarkus-run.jar` on a JRE as a non-root user.

## Test / lint

```bash
mvn -B verify                   # tests + checkstyle
```

## Layout

Five layers; each one depends only on the ones below it.

```
src/main/java/{{cookiecutter.java_package_dir}}/
├── Version.java       application version
├── api/               HTTP only — Jakarta REST resources; HealthResource, v1/ItemsResource
├── dto/               records that cross the HTTP boundary
├── service/           business rules; throw DomainException; no Jakarta REST imports
├── repository/        data access — one class per store, one method per query
└── core/              DomainException (+ NotFound, Validation), DomainExceptionMapper
src/test/java/…/
├── service/           rules, with a repository and no HTTP
└── api/               contract through REST Assured on @QuarkusTest
```

`api` calls `service`, never a repository. Services throw `DomainException` subclasses; `core/DomainExceptionMapper` answers `{"detail": {"code", "message", "field"}}`. The in-memory `ItemRepository` is the placeholder for a database or an external API.
