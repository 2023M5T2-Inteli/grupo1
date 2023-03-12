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
        primary: '#224957',
        action: '#20DF7F',
        background: '#E5E5E5',
      }
    },
  },
  plugins: [],
}
