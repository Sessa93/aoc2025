My personal collection of solutions for
[Advent of Code challenges 2025](https://adventofcode.com/2025)

## Using Docker
### Run tests
```
docker compose up --build test
```

### Run problems
```
docker compose up --build execute
```

### Get solution for specific day-problem combination
```
DAY=day-number PROBLEM=problem-number docker compose up --build execute
```

## Using uv
### Install dependencies
```
uv sync
```

### Run tests
```
uv run pytest
```

### Run all problems
```
PYTHONPATH=$(pwd) uv run python src/main.py run-all
```

### Get solution for specific day-problem combination
```
PYTHONPATH=$(pwd) uv run python src/main.py run-single --day day-number --problem problem-number
```

### Generate a new day template
```
uv run --script scripts/new-day.py day-number
```
