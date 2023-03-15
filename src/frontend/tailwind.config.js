/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    // "./src/renderer/index.html",
    // "./src/renderer/src/**/*.{js,ts,jsx,tsx}",
    // "./src/preload/index.js",
    // "./src/main/index.js",
    // "../electron-app/src/renderer/index.html",
    // "../electron-app/src/renderer/src/**/*.{js,ts,jsx,tsx}",
    // "../electron-app/src/preload/index.js",
    // "../electron-app/src/main/index.js",
    // "C:/Users/Inteli/repos/executable/electron-app/src/renderer/index.html",
    // "C:/Users/Inteli/repos/executable/electron-app/src/renderer/src/**/*.{js,ts,jsx,tsx}",
    // "C:/Users/Inteli/repos/executable/electron-app/src/preload/index.js",
    // "C:/Users/Inteli/repos/executable/electron-app/src/main/index.js",
    "./src/renderer/**/*.{js,ts,jsx,tsx}",
    "./**/*.html",
  ],
  theme: {
    extend: {
      fontFamily : {
        'montserrat' : ['Montserrat']
      },
      colors: {
        purple: '#2B1B53',
        action: '#20DF7F',
        background: '#E5E5E5',
      },
      gridTemplateColumns: {
        'sidebar-main-grid': 'auto 1fr'
      }
    },
  },
  plugins: [],
}
