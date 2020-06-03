module.exports = {
  ci: {
    collect: {
      url: ['http://localhost:3000/'],
      startServerCommand: 'jekyll build --config _config.yml',
    }
  }
}
