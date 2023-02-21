#!/usr/bin/node
const request = require('request');

// Get the movie ID from the first positional argument
const movieId = process.argv[2];

// Make a request to the Star Wars API for the movie details
const movieUrl = `https://swapi.dev/api/films/${movieId}/`;
request(movieUrl, (error, response, movieData) => {
  if (error) {
    console.error(error);
  } else {
    // Extract the list of characters from the movie details
    const characters = JSON.parse(movieData).characters;
    
    // Loop through the characters and print their names
    characters.forEach(characterUrl => {
      request(characterUrl, (error, response, characterData) => {
        if (error) {
          console.error(error);
        } else {
          const characterName = JSON.parse(characterData).name;
          console.log(characterName);
        }
      });
    });
  }
});
