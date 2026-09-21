<script setup lang="ts">
import { useFilmStore } from '../store';

const store = useFilmStore();

</script>
<template>
    <div id="film-details-modal" class="modal" :class="{ 'is-active': store.isModalOpen }">
        <div class="modal-background"></div>
        <div class="modal-card">
            <header class="modal-card-head">
                <p class="modal-card-title">{{ store.selectedFilm?.Title }}</p>
                <button class="delete" aria-label="close" @click="store.closeModal()"></button>
            </header>
            <section class="modal-card-body">
                <table class="table is-fullwidth">
                    <tbody>
                        <tr>
                            <th>Year</th>
                            <td>{{ store.selectedFilm?.Year }}</td>
                        </tr>
                        <tr>
                            <th>Rated</th>
                            <td>{{ store.selectedFilm?.Rated }}</td>
                        </tr>
                        <tr>
                            <th>Released</th>
                            <td>{{ store.selectedFilm?.Released }}</td>
                        </tr>
                        <tr>
                            <th>Genre</th>
                            <td>{{ store.selectedFilm?.Genre }}</td>
                        </tr>
                        <tr>
                            <th>Director</th>
                            <td>{{ store.selectedFilm?.Director }}</td>
                        </tr>
                        <tr>
                            <th>Writer</th>
                            <td>{{ store.selectedFilm?.Writer }}</td>
                        </tr>
                        <tr>
                            <th>Actors</th>
                            <td>{{ store.selectedFilm?.Actors }}</td>
                        </tr>
                        <tr>
                            <th>Plot</th>
                            <td>{{ store.selectedFilm?.Plot }}</td>
                        </tr>

                    </tbody>
                </table>
            </section>
            <footer class="modal-card-foot">
                <div class="buttons">
                    <button class="button" @click="store.closeModal()">Close</button>
                </div>
            </footer>
        </div>
    </div>
</template>