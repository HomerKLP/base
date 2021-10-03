# Base Project for starting Django projects

### Local deploy:

```bash
 $ docker-compose up -d
 ```

### Run tests:

```bash
$ docker-compose exec django bash
$ inv test

-- or --
 
$ docker-compose exec django inv test


-- to run certain test --

$ inv test -t test_example
```

### Run linter:

```bash
$ docker-compose exec django bash
$ inv lint

-- or --
 
$ docker-compose exec django inv lint
```

### API Documentation by Redoc

```
http://localhost:8000/docs/
```

### Django admin

```
http://localhost:8000/admin/
```
