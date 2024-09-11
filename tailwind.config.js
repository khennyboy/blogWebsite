/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./**/*.html", "./static/**/*.js"],
  theme: {
    extend: {
      fontFamily: {
        sans: ["Lato", "system-ui", "sans-serif"],
      },
    },
  },
  plugins: [],
};
