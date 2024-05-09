### ML Challenge

This is a learning project of ML it consists in create an API developed by vanilla python and explore each step such as routings, use cases, ingestions..

By default it follows DDD and hexagonal architecture

```md
src/
│
├── adapters/
│ ├── **init**.py
│ └── controllers/
│ └── user_controller.py
│
├── app/
│ ├── **init**.py
│ ├── repositories/
│ │ └── user_repository.py
│ ├── services/
│ │ └── external_service.py
│ ├── usecases/
│ └── user_usecase.py
│
└── domain/
├── **init**.py
└── entities/
```

## Todos

- [ x ] Create python API and document it by using open api
- [ ] Design target architecture as a diagram
- [ ] Make swagger to auto generated (Optional)
- [ ] Unit tests
