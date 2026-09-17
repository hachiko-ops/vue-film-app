export const API_URL = 'https://www.omdbapi.com/';
export const API_KEY = 'ad38cdaa';
export interface Film {
    Title: string;
    Year: string;
    imdbID: string;
    Type: string;
    Poster: string;
}

export interface OmdbResponse {
  Search: Film[];
  totalResults: number;
  Response: string;
}

export interface AppState {
  films: Film[];
  searchTerm: string;
}