# opswat-mono-repos

## System Architecture

### Back-end Architecture

1. Apply Clean Architecture and DDD for back-end source

### Font-end source architecture

1. Apply Atom design pattern for font-end source

## System initialization

### Start docker containers

```bash
docker-compose -f docker-compose.yml up -d
```

### Start Back-end service

1. Create virtual environment for python
2. Start this virtual environment and install required packages
   ```bash
   pip3 install -r requirements.txt
   ```
3. Start BE Service
   ```bash
   ENV=dev python3 -m uvicorn main:app --reload
   ```

### Start Font-end service

1. Install npm required dependencies
   ```bash
   yarn install
   ```
1. Start FE Service
   ```bash
   yarn start
   ```
