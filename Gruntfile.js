module.exports = function(grunt) {
  grunt.initConfig({
    watch: {
      frontend: {
        files: ['static/src/coffee/**/*.coffee'],
        tasks: ['coffee:frontend']
      },
      backend: {
        files: ['static/src/coffee/**/*.coffee'],
        tasks: ['coffee:backend']
      },
      styles: {
        files: ['static/src/less/**/*.less'],
        tasks: ['less']
      }
    },
    less: {
      dev: {
        options : {
          compress: true
        },
        files: {
          'static/build/css/style.css': ['static/src/less/**/*.less']
        }
      }
    },
    clean: {
      build: ['static/build/']
    },
    coffee: {
      static: {
        options: {
          join: true
        },
        files: {
          'static/build/js/app.js': ['static/src/coffee/**/*.coffee'],
        }
      }
    }
  });

  grunt.loadNpmTasks('grunt-contrib-less');
  grunt.loadNpmTasks('grunt-contrib-coffee');
  grunt.loadNpmTasks('grunt-contrib-watch');

  grunt.registerTask('default', ['coffee', 'less']);
};