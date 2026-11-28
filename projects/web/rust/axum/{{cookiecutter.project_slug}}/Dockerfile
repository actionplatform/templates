FROM rust:{{ cookiecutter._rust_version }}-slim-bookworm AS build
WORKDIR /app
COPY Cargo.toml Cargo.lock ./
COPY src ./src
RUN cargo build --release --locked

FROM gcr.io/distroless/cc-debian12:nonroot
COPY --from=build /app/target/release/{{ cookiecutter.package_name }} /app
ENV PORT=8000
EXPOSE 8000
USER nonroot
ENTRYPOINT ["/app"]
