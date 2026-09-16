<script setup lang="ts">
import { ref, watch } from 'vue';
import { debounce } from 'lodash-es';
import axios from 'axios';
import type { Film, OmdbResponse } from '../interfaces.ts';

const API_URL = 'https://www.omdbapi.com/';
const API_KEY = 'ad38cdaa';
  
const inputSearch = ref('');

const emit = defineEmits<{ 
  updateFilms: [films: Film[]] 
}>();

// Viene chiamata ogni volta che l'utente smette di scrivere per 300millisecondi
const updateDebounced = debounce(() => {
  searchMovie();
}, 300);

watch(inputSearch, (val:string) => {
  if( val.length > 2 ) {
    updateDebounced();
  }
})

async function searchMovie(){
  try {
    const response = await axios.get(API_URL, {
      params: {
        apikey: API_KEY,
        s: inputSearch.value
      }});
      const data = response.data as OmdbResponse;
  
      if( data.totalResults > 0 ) {
        emit('updateFilms', data.Search);
      }
  } catch (error) {
    console.error('Error fetching movies:', error);
  }

}
</script>

<template>
    <header class="section">
        <div class="columns">
            <div class="column is-one-third has-text-left">
              <h1 class="title">Found a movie</h1>
            </div>
            <div class="column">
                <div class="field has-addons">
                <div class="control is-expanded">
                    <input class="input" type="text" placeholder="Find a movie" v-model="inputSearch">
                </div>
                <div class="control">
                    <button class="button is-info" @click="searchMovie" >
                    Search
                    </button>
                </div>
                </div>
            </div>
        </div>
  </header>
</template>

