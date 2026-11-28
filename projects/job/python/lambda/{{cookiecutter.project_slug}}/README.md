# {{ cookiecutter.project_name }}

{% if cookiecutter.description %}{{ cookiecutter.description }}

{% endif %}An event handler on AWS Lambda, deployed with SAM. It runs when EventBridge fires its schedule or when SQS delivers a batch, logs to stdout (CloudWatch), reads its config from the environment and fails by raising: a failed schedule run is a failed invocation, a failed SQS record is reported back and retried, then moved to the dead-letter queue. No server stays running.

## Install

```bash
poetry install --with dev,code-quality
```

## Run

```bash
poetry run python -m app                        # scheduled event, events/schedule.json
poetry run python -m app events/sqs.json        # SQS batch
GREETING_NAME=Ada LOG_LEVEL=DEBUG poetry run python -m app
```

| Variable | Default | Effect |
|---|---|---|
| `LOG_LEVEL` | `INFO` | logging level |
| `GREETING_NAME` | `world` | who the example task greets; empty makes the job fail |

Both are template parameters (`LogLevel`, `GreetingName`); see `.env.example`.

## Test / lint

```bash
poetry run pytest
poetry run ruff check .
poetry run ruff format --check .
poetry run mypy --config-file .code_quality/mypy.ini .
sam validate --lint
```

## SAM

```bash
sam build
sam local invoke JobFunction -e events/schedule.json      # needs Docker
sam local invoke JobFunction -e events/sqs.json
sam deploy --guided
```

`template.yaml` declares one function with two triggers: a `Schedule` (`rate(1 day)`, parameter `Schedule`) and an SQS queue with a dead-letter queue after 3 receives. `.github/workflows/sam-validate.yml` runs `sam validate --lint` and `sam build` on GitHub; on the other CI providers run the same two commands.

## Layout

```
app/
├── __init__.py      __version__
├── __main__.py      runs the handler locally on an event file
├── handler.py       Lambda entrypoint: schedule or SQS batch
└── task.py          the work: reads env, raises on failure
events/              sample events for sam local invoke and python -m app
template.yaml        SAM: function, schedule, queue, dead-letter queue
samconfig.toml
tests/
└── test_job.py
```
