# vue-film-app

A Vue 3 application built with Vite.

## Project setup

Install the project dependencies:

```bash
npm install
```

## Development

Start the development server with hot reload:

```bash
npm run dev
```

The application will be available at:

http://localhost:5173/

## Production build

Build the application for production:

```bash
npm run build
```

Preview the production build locally:

```bash
npm run preview
```

## Linting

Run ESLint:

```bash
npm run lint
```

## Docker

Build the Docker image:

```bash
docker build -t vue-film-app .
```

Run the application in a Docker container:

```bash
docker run -p 8080:80 vue-film-app
```

The application will be available at:

http://localhost:8080/

## Project structure

```text
vue-film-app/
├── public/
├── src/
├── index.html
├── vite.config.js
├── Dockerfile
├── .dockerignore
├── package.json
└── package-lock.json
```

## Technologies

- Vue 3
- Vite
- Axios
- Bulma
- ESLint
- Docker