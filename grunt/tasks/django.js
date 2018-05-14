/* jshint node: true */
'use strict';

var fs = require('fs'),
	childProcess = require('child_process');

// Get your ip address
function ip() {
	var interfaces = require('os').networkInterfaces(),
		out = '0.0.0.0';

	Object.keys(interfaces).forEach(function (key) {
		interfaces[key].forEach(function (item) {
			if (item.family === 'IPv4' && item.address !== '127.0.0.1' && !item.internal) {
				out = item.address;
			}
		});
	});

	return out;
}

module.exports = function (grunt) {
	grunt.registerTask('django', 'An alias for Django runserver', function (arg1) {
		var port = arg1 || grunt.config.get('django.port'),
			server;

		grunt.config('watch.livereload.options.livereload', Math.round(port) + 30000);

		// Don't run the server if the project has not been setup.
		if (!fs.existsSync('env/bin/activate')) {
			grunt.log.error([
				'This project does not seem to be set up yet.',
				'Check the README.md for setup info.',
				'',
				'If you are just starting the project,',
				'you will likely need to run the following.',
				'',
				'sh ./scripts/setup.sh'
			].join('\n'));
			return;
		}

		function kill() {
			server.kill();
		}

		process.on('exit', kill).on('SIGINT', kill).on('uncaughtException', kill);

		// Start up the Django server.
		// This will run `sh ./scripts/run.sh`, passing in the specified port.
		server = childProcess.spawn('sh', ['./scripts/run.sh', '0.0.0.0:' + port], { stdio: 'inherit' });

		// Open a browser. Wait a couple seconds to allow the server to start.
		setTimeout(function () {
			childProcess.exec('open http://' + ip() + ':' + port);
		}, 2000);
	});
};
