<script setup>


import { ref, onMounted } from "vue";

onMounted(() => {
    getCsrfToken();
});

let csrf_token = ref("");
    function getCsrfToken() {

        fetch('/api/v1/csrf-token')
            .then((response) => response.json())
            .then((data) => {
                console.log(data);
                csrf_token.value = data.csrf_token;
            })
    }

const saveMovie = () => {
    let movieForm = document.getElementById('movieForm');
    let form_data = new FormData(movieForm);

    fetch("/api/v1/movies", {
        method: 'POST',
        body: form_data,
        headers: {
            'X-CSRFToken': csrf_token.value
        }
    })
    .then(function (response) {
        return response.json();
    })
    .then(function (data) {
        // display a success message
        console.log(data);
    })
    .catch(function (error) {
        console.log(error);
    });
};
</script>



<template>
    <form @submit.prevent="saveMovie" id="movieForm">
        <div class="form-group mb-3">
            <label for="title" class="form-label">Movie Title</label>
            <input type="text" name="title" class="formcontrol" />
        </div>
        <div class="form-group mb-3">
            <label for="description" class="form-label">Movie Description</label>
            <input type="text" name="description" class="formcontrol" />
        </div>
        <div class="form-group mb-3">
            <label for="poster" class="form-label">Movie Poster</label>
            <input type="image" name="poster" class="formcontrol" />
        </div>

        <button class="btn btn-primary" type="submit">Add</button>
    </form>
</template>