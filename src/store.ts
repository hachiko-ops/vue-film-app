import { defineStore } from 'pinia';
import axios from 'axios';
import type { Film, AppState } from './interfaces.ts';
import { API_URL, API_KEY } from './interfaces';

export const useFilmStore = defineStore('filmStore', {
    state: () => ({
        films: [] as Film[],
        searchTerm: '',
        selectedFilm: null as Film | null,
        isModalOpen: false
    } as AppState),

    actions: {
        openModal(film: Film) {
            this.isModalOpen = true;
            getFilmDetails(film);
        },
        closeModal() {
            this.isModalOpen = false;
            this.selectedFilm = null;
        }
    }
});

async function getFilmDetails( film: Film){
  try {
    const response = await axios.get<Film>(API_URL, {
      params: {
        apikey: API_KEY,
        i: film.imdbID
      }});
      const details = response.data;
      useFilmStore().selectedFilm = details;

  } catch (error) {
    console.error('Error fetching details movie:', error);
  }

}
