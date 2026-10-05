<script lang="ts" setup>
import {ref} from 'vue';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { faComment } from '@fortawesome/free-solid-svg-icons'
import { useFilmStore } from '../store';

const store = useFilmStore();
const newUserMessage = ref('');

const sendMessage = () => {
    if (newUserMessage.value.trim() !== '') {
        store.addMessage(newUserMessage.value);
        newUserMessage.value = '';
    }
}
</script>
<template>
    <button id="chat-toggle" class="button is-primary is-rounded chat-trigger-btn"
        :class="{'is-hidden': store.isChatOpen}" @click="store.openChat()">
        <span class="icon is-medium">
            <FontAwesomeIcon :icon="faComment" size="lg" />
        </span>
    </button>

    <!-- FINESTRA DI CHAT FLUTTUANTE -->
    <div id="chat-window" class="panel is-link" :class="{ 'is-hidden': !store.isChatOpen }">

        <!-- Intestazione della Chat -->
        <header class="panel-heading is-flex is-justify-content-space-between is-align-items-center">
            <div class="">
                <strong class="has-text-white ml-2">Assistenza Clienti</strong>
            </div>
            <!-- Pulsante per chiudere direttamente dall'header -->
            <button id="chat-close" class="delete is-medium" @click="store.closeChat()"></button>
        </header>

        <!-- Corpo della Chat (Scrollabile) -->
        <div v-for="message in store.chatMessages" :key="message.id"
            class="panel-block is-flex-direction-column align-items-stretch">
            <div class="is-flex align-self-start mb-2">
                <div class="message "
                    :class="{ 'is-info': message.sender === 'assistant', 'is-success': message.sender === 'user' }">
                    <div class="message-body">
                        {{ message.text }}
                    </div>
                </div>
            </div>
        </div>

        <!-- Footer della Chat (Form di Input) -->
        <footer class="panel-block">
            <div class="field has-addons">
                <div class="control">
                    <input class="input is-rounded is-small" type="text" placeholder="Write a message..."
                        v-model="newUserMessage">
                </div>
                <div class="control">
                    <button class="button is-primary is-rounded is-small" @click="sendMessage">
                        <span class="icon">
                            <i class="fas fa-paper-plane"></i>
                        </span>
                    </button>
                </div>
            </div>
        </footer>

    </div>
</template>