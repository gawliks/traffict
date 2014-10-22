 requirejs.config({
     baseUrl: 'lib',
     paths: {
         jquery: 'vendor/jquery',
         app: '../app',
         foundation: 'vendor/foundation.min',
         knockout: 'vendor/knockout',
         vmfactory: 'vmfactory'
     },
     shim: {
         foundation: {
             deps: ['jquery'],
         }
     }
 });
console.log('config');
requirejs(["app"], function() {
    console.log('app loaded');
    $(document).foundation();
    //new App();
});