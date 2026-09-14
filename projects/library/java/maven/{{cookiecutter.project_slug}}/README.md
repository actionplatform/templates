# {{ cookiecutter.project_name }}

{{ cookiecutter.description }}

## Install

```xml
<dependency>
  <groupId>{{ cookiecutter.java_package }}</groupId>
  <artifactId>{{ cookiecutter.project_slug }}</artifactId>
  <version>0.0.0</version>
</dependency>
```

## Develop

```bash
mvn -B verify        # compile, test, checkstyle
```

## Layout

```
src/main/java/{{cookiecutter.java_package_dir}}/   # Hello (dummy), Version
src/test/java/{{cookiecutter.java_package_dir}}/   # JUnit 5
.code_quality/checkstyle.xml
```
