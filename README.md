### ML Challenge

This is a learning project of ML it consists in create an API developed by vanilla python and explore each step such as routings, use cases, ingestions..

By default it follows DDD and hexagonal architecture

### Running app locally

Create a virtual environment

```console
python3 -m venv venv
```

Activate the virtual environment

```console
source venv/bin/activate
```

Install dependencies

```console
python3 -m pip install -r requirements.txt
```

Run application

```console
python3 src/
```

it runs on http://localhost:8000/

### Specification folder

There is a swagger file with all resources documented

easy way to test with a running application:
open https://editor.swagger.io/ and paste content of specification/swagger.yaml

## Todos

- [ x ] Create python API and document it by using open api
- [ ] Design target architecture as a diagram
- [ ] Make swagger to auto generated (Optional)
- [ ] Unit tests
