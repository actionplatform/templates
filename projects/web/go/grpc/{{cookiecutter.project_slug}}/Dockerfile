FROM golang:{{ cookiecutter._go_version }} AS build
WORKDIR /src
COPY go.mod go.sum ./
RUN go mod download
COPY . .
RUN CGO_ENABLED=0 go build -trimpath -o /out/server ./cmd/server

FROM gcr.io/distroless/static-debian12:nonroot
COPY --from=build /out/server /server
ENV PORT=8000 GRPC_PORT=50051
EXPOSE 8000 50051
ENTRYPOINT ["/server"]
