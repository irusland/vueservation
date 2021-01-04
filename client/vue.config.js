module.exports = {
  devServer: {
    proxy: {
      '^/api': {
        target: 'http://0.0.0.0:8080/hello',
        changeOrigin: true,
        secure:false,
        pathRewrite: {'^/api': '/api'},
        logLevel: 'debug'
    },
    }
  }
}
