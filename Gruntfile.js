/*jshint node:true*/
'use strict';

var CONFIG = {
	source : 'project/source/',
	static : 'project/static/',
	templates : 'project/templates/'
};

module.exports = function (grunt) {
	require('time-grunt')(grunt);
	require('jit-grunt')(grunt, {
		sprite: 'grunt-spritesmith'
	})({
		loadTasks: 'grunt/tasks'
	});

	[
		'autoprefixer',
		'clean',
		'copy',
		'django',
		'emberTemplates',
		'jshint',
		'neuter',
		'modernizr',
		'notify',
		'sass',
		'sprite',
		'uglify',
		'watch',
		'webfont'
	].forEach(function (key) {
		grunt.config(key, require('./grunt/config/' + key)(CONFIG));
	});

	grunt.registerTask('server', function (port) {
		if (port) {
			grunt.config('django.port', port);
		}

		grunt.task.run([
			// Run tasks once before starting watchers
			'develop',

			// Start server
			'django',

			// Watch files for changes
			'watch'
		]);
	});

	// Build unminified files during development
	grunt.registerTask('develop', [
		'clean',

		// JS
		'neuter:libsDevelop',
		'neuter:app',
		'neuter:tests',
		'emberTemplates',

		// CSS
		'sass:develop',
		'autoprefixer:develop',
		'fixSourceMaps',

		// OTHER FILES
		'copy'
	]);

	// Build minified files for deployment
	grunt.registerTask('build', [
		'clean',

		// JS
		'jshint',
		'neuter:libsBuild',
		'neuter:app',
		'modernizr',
		'emberTemplates',
		'uglify',

		// CSS
		'sass:build',
		'autoprefixer:build',

		// TEMP FOLDER
		'clean:temp',

		// OTHER FILES
		'copy',
		'notify:build'
	]);

	grunt.registerTask('default', ['build']);
};
