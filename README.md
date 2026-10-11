# Vue Film App

A movie discovery application built with Vue 3 and TypeScript, with a Django backend for experimenting with AI-powered, natural-language film search.

The project combines a movie discovery interface, a personal wishlist, and an AI-powered backend that uses Google Gemini to interpret search requests and extract structured criteria. It is also a hands-on project for exploring Python, Django, API integration, and the evaluation of AI-generated results.

## Features

### Frontend
- **Movie search:** Search the OMDb catalogue by title.
- **Debounced search:** Avoid unnecessary requests while typing.
- **Film details:** View information such as release year, genre, director, actors, and plot in a modal.
- **Wishlist:** Add or remove films and persist the list in browser `localStorage`.
- **Floating chat interface:** A chat-style UI with a message list and input field.

### Backend and AI
- **Natural-language query parsing:** Use Google Gemini to extract structured search criteria from a natural-language request.
- **Structured AI responses:** Extract information such as genre, release year, director, actors, language, and an explanation of the interpretation.
- **Film lookup:** Integrate with OMDb to retrieve film details and check suggested titles.
- **Search quality tracking:** Store search information and track titles that cannot be found, supporting further analysis of AI-generated suggestions.

### Development environment
- **Containerized setup:** Run the Vue frontend and Django backend as separate services using Docker Compose.

> **Current status:** The frontend movie discovery features and the Django AI-search backend are under development. The backend includes Gemini-based query interpretation and OMDb integration. The floating chat interface is not yet connected to the backend search endpoint.

## Tech stack

### Frontend
- Vue 3
- TypeScript
- Vite
- Pinia
- Axios
- Bulma
- Font Awesome
- Lodash

### Backend
- Python 3.13
- Django
- Google Gen AI SDK (Gemini)
- Requests (HTTP client)
- SQLite

### Development tools
- Docker
- Docker Compose
- ESLint

## Project structure

```text
vue-film-app/
├── backend/
│   ├── config/          # Django project configuration
│   ├── films/           # Film search, AI integration, and API logic
│   ├── public/          # Public views and templates
│   ├── Dockerfile
│   ├── manage.py
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── components/  # Search, film cards, details modal, chat UI
│   │   ├── App.vue
│   │   ├── interfaces.ts
│   │   └── store.ts     # Pinia application state
│   ├── Dockerfile
│   └── package.json
└── compose.yaml
```

## Requirements

- Docker and Docker Compose
- An OMDb API key
- A Google Gemini API key

## Getting started

### 1. Configure environment variables

Clone the repository and navigate to the project directory.

Create a `backend/.env` file with the credentials required by the backend:

```env
GEMINI_API_KEY=your_gemini_api_key
OMDB_API_KEY=your_omdb_api_key
```

Make sure the Django settings load these environment variables and that the `.env` file is excluded from version control.

### 2. Start the application

Run the following command from the project root:

```bash
docker compose up --build
```

### 3. Open the application

- **Frontend:** http://localhost:5173
- **Django backend:** http://localhost:8000

The Compose configuration mounts the source directories into the containers, allowing code changes to be picked up during development.

## AI search endpoint

The Django backend exposes an endpoint for interpreting natural-language film searches.

```http
GET /api/films/search?s=<natural-language-query>
```

Example:

```bash
curl --get "http://localhost:8000/api/films/search" \
  --data-urlencode "s=Find a comedy from the 1980s"
```

Gemini interprets the query and extracts structured search criteria, including:

- `title`
- `genre`
- `year`
- `director`
- `actors`
- `language`
- `reason`

The `reason` field explains how the natural-language request was interpreted.

The endpoint returns HTTP 400 when the search parameter is missing or shorter than three characters, and HTTP 405 for unsupported HTTP methods.

The AI and film-lookup services are being developed to support validation of suggested titles and the collection of search-quality metrics.

## Frontend development

To run the frontend outside Docker, navigate to the `frontend/` directory:

```bash
npm install
npm run dev
```

Available scripts:

```bash
npm run build    # Create a production build
npm run preview  # Preview the production build
npm run lint     # Run ESLint
```

## Notes

- The wishlist is stored in browser `localStorage` and is not synchronized across browsers or devices.
- The chat interface is not yet connected to the Django backend.
- AI-generated criteria and film suggestions may require validation; the project explores ways to measure and improve result quality.
- API keys must never be committed to source control. Keep external API credentials on the server and configure them through environment variables.
