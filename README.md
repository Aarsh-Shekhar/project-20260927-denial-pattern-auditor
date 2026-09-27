# Denial Pattern Auditor

Finds recurring denial patterns in synthetic billing events.

## What it includes

- deterministic sample data
- scoring and ranking logic
- command line report
- unit tests
- continuous validation workflow

## Run

```bash
python3 -m denial_pattern_auditor.cli --input data/sample_denials.json
```

## Test

```bash
python3 -m unittest discover tests
```
