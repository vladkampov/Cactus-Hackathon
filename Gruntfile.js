module.exports = function(grunt) {
  grunt.initConfig({
    watch: {
      scripts: {
        files: ['static/src/coffee/**/*.coffee'],
        tasks: ['coffee:static']
      },
      styles: {
        files: ['static/src/less/**/*.less'],
        tasks: ['less:dev']
      }
    },
    less: {
      dev: {
        options : {
          compress: true
        },
        files: {
          'static/build_grunt/css/style.css': ['static/src/less/**/*.less']
        }
      }
    },
    coffee: {
      static: {
        options: {
          join: true
        },
        files: {
          'static/build_grunt/js/app.js': ['static/src/coffee/**/*.coffee'],
        }
      }
    },
    concat: {
      libs: {
        files: {
          'static/build_grunt/js/libs.js': ['node_modules/jquery/dist/jquery.min.js', 'node_modules/bootstrap/dist/js/bootstrap.min.js'],
          'static/build_grunt/css/libs.css': ['node_modules/bootstrap/dist/css/bootstrap.min.css']
        }
      }
    }
  });

  grunt.loadNpmTasks('grunt-contrib-less');
  grunt.loadNpmTasks('grunt-contrib-coffee');
  grunt.loadNpmTasks('grunt-contrib-watch');
  grunt.loadNpmTasks('grunt-contrib-concat');

  grunt.registerTask('default', ['coffee', 'less', 'concat']);
};