/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
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
