/*jshint node:true*/
'use strict';

// https://github.com/Modernizr/grunt-modernizr

// Sifts through your project files, gathers up your references
// to Modernizr tests and outputs a lean, mean Modernizr machine.

module.exports = function (config) {
	return {
		build : {
			devFile : config.source + 'lib/modernizr/modernizr.js',
			outputFile : config.static + 'lib/modernizr/modernizr.js',
			files : {
				src : [
					config.source + 'js/**/*.js',
					config.source + 'scss/**/*.scss'
				]
			}
		}
	};
};
