import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import history from 'connect-history-api-fallback';

// https://vitejs.dev/config/
export default defineConfig({
  // GitHub Pages 部署路径：https://<username>.github.io/spuseum/
  // 本地开发时 base='/' 也可用，这里先用 './' 兼容两种情况
  base: './',
  plugins: [react()],
  server: {
    middleware: [history()],
  },
});
