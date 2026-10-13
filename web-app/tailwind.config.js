/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        dark: {
          base: '#121316',
          surface: '#1a1b20',
          elevated: '#22242c',
          card: '#1f2027',
          hover: '#2a2c36',
          border: '#2d2f3a'
        }
      }
    },
  },
  plugins: [],
}
