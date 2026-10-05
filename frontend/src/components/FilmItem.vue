<script setup lang="ts">
import type { Film } from '../interfaces.ts';
import { useFilmStore } from '../store';

const props = defineProps<{ film: Film }>();
const film = props.film;
const store = useFilmStore();

</script>
<template>
    <div class="card">
        <div class="card-image">
            <figure class="image is-4by3">
                <img :src="film.Poster" :alt="film.Title" />
            </figure>
        </div>
        <div class="card-content">

            <div class="content">
                <h3 class="is-size-4">{{ film.Title }}</h3>
                <br />
                <span class="is-uppercase is-size-6 has-text-grey">{{ film.Type }}</span> -
                <time :datetime="film.Year">{{ film.Year }}</time>
            </div>
        </div>
        <div class="card-footer">
            <a href="#" class="card-footer-item" @click="store.openModal(film)" >View Details</a>
            <a href="#" class="card-footer-item" @click="store.toggleWishlistItem(film)" >
                <span v-if="store.isInWishlist(film)">Remove from Wishlist</span>
                <span v-else>Add to Wishlist</span>
            </a>
        </div>
    </div>
</template>
