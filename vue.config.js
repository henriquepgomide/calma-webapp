module.exports = {
  publicPath: process.env.NODE_ENV === "production" ? "/" : "/",
  pwa:{
    themeColor: '#209cee',
    workboxPluginMode: 'InjectManifest',
    workboxOptions: {
      swSrc: 'service-worker.js',
    },
  }
};
