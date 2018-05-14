/*jshint node:true*/
'use strict';

// https://github.com/dgeb/grunt-ember-templates

// Precompile Handlebars templates for Ember.js.

module.exports = function (config) {
	return {
		options : {
			templateBasePath: config.source + 'templates/',
			templateCompilerPath: config.source + 'lib/ember/ember-template-compiler.js',
			handlebarsPath: config.source + 'lib/handlebars/handlebars.js'
		},
		templates: {
			src: config.source + 'templates/{,*/}*.hbs',
			dest: config.static + 'js/templates.develop.js'
		}
	};
};
