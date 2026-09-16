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