# python-api-projects

REST API development with FastAPI — routing, middleware, authentication, and external service integrations.

## Structure

\\\
python-api-projects/
├── src/
│   ├── routes/       # FastAPI routers (endpoints)
│   ├── models/       # Pydantic request/response models
│   ├── services/     # Business logic layer
│   └── middleware/   # Auth, logging, CORS middleware
├── notebooks/        # API exploration and prototyping
├── tests/            # Pytest + httpx async tests
├── .gitignore
├── requirements.txt
├── main.py           # FastAPI app entrypoint
└── README.md
\\\

## Projects

| Project | Description | Status |
|---------|-------------|--------|
| ML Inference API | FastAPI wrapper around sklearn/PyTorch models |  In Progress |
| Auth Service | JWT-based auth with FastAPI + Pydantic v2 |  In Progress |
| External Integrations | REST client patterns for third-party APIs |  In Progress |

## Setup

\\\ash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
\\\

## Tech Stack
- Python 3.11+, FastAPI, Uvicorn
- Pydantic v2, SQLAlchemy, Alembic
- HTTPX, Requests
- Pytest, pytest-asyncio
