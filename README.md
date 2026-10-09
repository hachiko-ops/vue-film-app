# Vue Film App

A movie discovery application built with Vue 3 and TypeScript. It lets users search for films, view detailed information, save titles to a wishlist, and experiment with natural-language search parsing using Gemini.

## Features

- **Movie search:** search the OMDb catalogue by title.
- **Debounced search:** typing pauses trigger a search after a short delay.
- **Film details:** open a modal with information such as release date, genre, director, actors, and plot.
- **Wishlist:** add or remove films and keep the wishlist in browser `localStorage`.
- **Floating chat interface:** a chat widget UI with a message list and input.
- **AI search-query parsing (backend):** a Django endpoint uses Google Gemini to extract structured search filters from a natural-language query, including title, genre, release year, director, actors, and language.
- **Containerized development:** Docker Compose runs the Vue frontend and Django backend as separate services.

> **Current status:** the Gemini query-parsing endpoint is implemented in the backend. The floating chat UI currently manages messages in the frontend store; it is not yet connected to the Gemini endpoint.

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
- SQLite (Django's default database configuration)

### Development tools
- Docker and Docker Compose
- ESLint

## Project structure

```text
vue-film-app/
├── backend/
│   ├── config/          # Django project configuration
│   ├── films/           # Film search and Gemini query parsing endpoint
│   ├── public/          # Public Django views and templates
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
- An OMDb API key for movie search
- A Google Gemini API key for the AI query-parsing endpoint

## Run with Docker Compose

1. Clone the repository and open the project directory.
2. Create `backend/.env` and add your Gemini API key:

   ```env
   GEMINI_API_KEY=your_gemini_api_key
   ```

3. Start both services:

   ```bash
   docker compose up --build
   ```

4. Open the frontend at [http://localhost:5173](http://localhost:5173). The Django backend is available at [http://localhost:8000](http://localhost:8000).

The Compose configuration mounts the source directories into the containers, so code changes are available during development.

## AI search-query endpoint

The backend exposes a GET endpoint at:

```text
/api/films/search?s=<natural-language-query>
```

Example:

```bash
curl --get "http://localhost:8000/api/films/search" \
  --data-urlencode "s=Find a comedy from the 1980s"
```

Gemini is prompted to return a JSON object containing these fields:

- `title`
- `genre`
- `year`
- `director`
- `actors` (list)
- `language`
- `reason` (short explanation of the extracted filters)

The endpoint returns HTTP 400 if the search parameter is missing or shorter than three characters, and HTTP 405 for methods other than GET.

## Frontend commands

Run these commands from the `frontend/` directory:

```bash
npm install
npm run dev
```

Other available scripts:

```bash
npm run build  # Create a production build
npm run preview # Preview the production build
npm run lint   # Run ESLint
```

## Notes

- The wishlist is stored in the browser's `localStorage`; it is not synced across browsers or devices.
- The AI endpoint currently extracts search criteria; it does not yet execute a database search or return matching films.
- Keep API keys out of source control. For production, move external API credentials out of frontend code and configure them securely on the server.
