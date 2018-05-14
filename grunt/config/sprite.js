/*jshint node:true*/
'use strict';

// https://github.com/Ensighten/grunt-spritesmith

// Convert a set of images into a spritesheet and corresponding CSS variables.

module.exports = function (config) {
	return {
		application: {
			src: config.source + 'img/sprites-source/application/**/*.png',
			dest: config.source + 'img/sprites/application.png',
			destCss: config.source + 'scss/sprites/_application.scss',
			padding: 20,
			imgPath: '../img/sprites/application.png',
			cssFormat: 'scss'
		}
	};
};
