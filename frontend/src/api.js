import axios from 'axios';

// Use environment variable for API URL, fallback to localhost for development
const BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';

export async function generateNarration(poi) {
  const response = await axios.post(`${BASE_URL}/generate_narration?poi=${encodeURIComponent(poi)}`);
  return response.data.narration;
}

// Add function for route generation
export async function generateRoute(inputText, context = null) {
  const response = await axios.post(`${BASE_URL}/generate-route`, {
    input_text: inputText,
    context: context
  });
  return response.data;
}

// Add function for roam feature
export async function generateRoam(coordinates, context = null) {
  const response = await axios.post(`${BASE_URL}/roam`, {
    coordinates: coordinates,
    context: context
  });
  return response.data;
}

// Add function for weather
export async function getWeather(lat, lon) {
  const response = await axios.get(`${BASE_URL}/weather?lat=${lat}&lon=${lon}`);
  return response.data;
}