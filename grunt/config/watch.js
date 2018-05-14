/*jshint node:true*/
'use strict';

// https://github.com/gruntjs/grunt-contrib-watch

// Run tasks whenever files are changed, added, or deleted.

module.exports = function (config) {
	return {
		sass: {
			files: [config.source + 'scss/{,**/}{,*.scss,*.sass}'],
			tasks: ['sass:develop', 'autoprefixer:develop', 'fixSourceMaps']
		},
		emberTemplates: {
			files: config.source + 'templates/{,**/}{,*.hbs}',
			tasks: ['emberTemplates']
		},
		neuter: {
			files: [config.source + 'js/{,**/}{,*.js}'],
			tasks: ['neuter:app']
		},
		neuterLibs: {
			files: [config.source + 'js/libs.js'],
			tasks: ['neuter:libsDevelop']
		},
		neuterTests: {
			files: [config.source + 'tests/{,**/}{,*.js}'],
			tasks: ['neuter:tests']
		},
		livereload: {
			options: {
				livereload: 34567
			},
			files: [
				config.templates + '{,**/}*.html',
				config.static + '{,**/}*.{css,js,png,jpg,jpeg,gif,webp,svg}',
				config.source + '{,**/}*.{png,jpg,jpeg,gif,webp,svg}'
			]
		}
	};
};
