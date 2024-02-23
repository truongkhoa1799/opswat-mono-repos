# opswat-mono-repos

## Start docker containers

```bash
docker-compose -f docker-compose.yml up -d
```

## Start Backend service

```sh
workon python312
ENV=dev python3 -m uvicorn main:app --reload
```
