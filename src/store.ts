import { defineStore } from 'pinia';
import type { Film, AppState } from './interfaces.ts';

export const useFilmStore = defineStore('filmStore', {
    state: () => ({
        films: [] as Film[],
        searchTerm: ''
    } as AppState),
});