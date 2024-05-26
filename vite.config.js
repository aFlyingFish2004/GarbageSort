import { fileURLToPath, URL } from 'node:url'
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import fs from 'fs'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    vue(),
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  },
  server: {
    host: '10.122.210.57',
    port: 5173,
    https: {
      key: fs.readFileSync('./certificates/private.key'),
      cert: fs.readFileSync('./certificates/certificate.crt'),
    }
  }
})