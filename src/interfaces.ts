export const API_URL = 'https://www.omdbapi.com/';
export const API_KEY = 'ad38cdaa';
export interface Film {
    Title: string;
    Year: string;
    Rated: string;
    Released: string;
    Genre: string;
    Director: string;
    Writer: string;
    Actors: string;
    Plot: string;
    imdbID: string;
    Type: string;
    Poster: string;
    Language: string;
    Contry: string;
    Awards: string;
    Ratings: { Source: string; Value: string }[];
    Metascore: string;
    imdbRating: string;
    imdbVotes: string;
    DVD: string;
    BoxOffice: string;
    Production: string;
    Website: string;
    Response: string;
}

export interface OmdbResponse {
  Search: Film[];
  totalResults: number;
  Response: string;
}

export interface AppState {
  films: Film[];
  searchTerm: string;
  selectedFilm: Film | null;
  isModalOpen: boolean;
  wishlist: Film[];
  showWishlist: boolean;
}