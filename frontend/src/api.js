import axios from 'axios';

const BASE_URL = 'https://passepartout-1.onrender.com';

export async function generateNarration(poi) {
  const response = await axios.post(`${BASE_URL}/generate_narration?poi=${encodeURIComponent(poi)}`);
  return response.data.narration;
}