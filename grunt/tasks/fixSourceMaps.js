/* jshint node: true */
'use strict';

module.exports = function (grunt) {
	grunt.config('fixSourceMaps', {
		develop: {
			src : 'project/static/css/**/*.map'
		}
	});

	// Because both the source and static folders
	// are served by django with the /static/ path,
	// we want to make sure the sourcemaps point to
	// static/scss/style.scss instead of
	// source/scss/style.scss
	function replaceSourceFolder(path) {
		return path.replace('../../project/source/', '');
	}

	function handleFile(file) {
		var source = grunt.file.readJSON(file);
		source.sources = source.sources.map(replaceSourceFolder);
		grunt.file.write(file, JSON.stringify(source));
	}

	function handleFiles(files) {
		files.src.forEach(handleFile);
	}

	grunt.registerMultiTask('fixSourceMaps', 'Convert `../source` urls in the sass source maps to `../static`', function () {
		this.files.forEach(handleFiles);
	});
};
