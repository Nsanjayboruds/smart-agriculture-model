const inputBox = document.querySelector('.input-box');
const searchBtn = document.getElementById('searchBtn');
const weather_img = document.querySelector('.weather-img');
const temperature = document.querySelector('.temperature');
const description = document.querySelector('.description');
const humidity = document.getElementById('humidity');
const wind_speed = document.getElementById('wind-speed');

const location_not_found = document.querySelector('.location-not-found');
const weather_body = document.querySelector('.weather-body');

const forecastContainer = document.querySelector('.forecast'); // add in HTML

const api_key = "4c4286de4f6a3794841e570fd8bc4a0b";

// 🌤️ Current Weather
async function checkWeather(city) {
    try {
        showLoading();

        const url = `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${api_key}`;
        const res = await fetch(url);
        const data = await res.json();

        if (data.cod !== 200) {
            showError();
            return;
        }

        updateUI(data);
        getForecast(city);

    } catch (error) {
        console.error(error);
        showError();
    }
}

// 📅 5-Day Forecast (REAL PREDICTION)
async function getForecast(city) {
    const url = `https://api.openweathermap.org/data/2.5/forecast?q=${city}&appid=${api_key}`;
    const res = await fetch(url);
    const data = await res.json();

    forecastContainer.innerHTML = "";

    const dailyData = data.list.filter(item =>
        item.dt_txt.includes("12:00:00")
    );

    dailyData.forEach(day => {
        const div = document.createElement("div");
        div.classList.add("forecast-card");

        div.innerHTML = `
            <p>${new Date(day.dt_txt).toDateString().slice(0, 10)}</p>
            <img src="https://openweathermap.org/img/wn/${day.weather[0].icon}@2x.png">
            <h3>${Math.round(day.main.temp - 273.15)}°C</h3>
            <p>${day.weather[0].main}</p>
        `;

        forecastContainer.appendChild(div);
    });
}

// 📍 Auto location weather
function getLocationWeather() {
    navigator.geolocation.getCurrentPosition(async (position) => {
        const { latitude, longitude } = position.coords;

        const url = `https://api.openweathermap.org/data/2.5/weather?lat=${latitude}&lon=${longitude}&appid=${api_key}`;

        const res = await fetch(url);
        const data = await res.json();

        updateUI(data);
        getForecast(data.name);
    });
}

// 🔄 UI Update
function updateUI(weather_data) {
    location_not_found.style.display = "none";
    weather_body.style.display = "flex";

    temperature.innerHTML = `${Math.round(weather_data.main.temp - 273.15)}°C`;
    description.innerHTML = weather_data.weather[0].description;
    humidity.innerHTML = `${weather_data.main.humidity}%`;
    wind_speed.innerHTML = `${weather_data.wind.speed} Km/H`;

    const main = weather_data.weather[0].main.toLowerCase();

    const icons = {
        clouds: "img/cloud.png",
        clear: "img/clear-sky.png",
        rain: "img/rain.png",
        drizzle: "img/rain.png",
        mist: "img/mist.png",
        haze: "img/mist.png",
        fog: "img/mist.png",
        snow: "img/snow.png",
        thunderstorm: "img/thunderstorm.png"
    };

    weather_img.src = icons[main] || "img/default.png";
}

// ❌ Error UI
function showError() {
    location_not_found.style.display = "block";
    weather_body.style.display = "none";
}

// ⏳ Loading UI
function showLoading() {
    location_not_found.style.display = "none";
    weather_body.style.display = "flex";
    temperature.innerHTML = "Loading...";
}

// 🔘 Button click
searchBtn.addEventListener('click', () => {
    const city = inputBox.value.trim();
    if (city) checkWeather(city);
});

// ⌨️ Enter key support
inputBox.addEventListener("keypress", (e) => {
    if (e.key === "Enter") {
        checkWeather(inputBox.value.trim());
    }
});

// 📍 Auto load user location weather
window.addEventListener("load", getLocationWeather);