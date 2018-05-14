/*
	Invoke an Handlebars helper.

	invokeHelper('my-helper', value)
*/

Ember.Test.registerHelper('invokeHelper', function (app, helperName, parameter) {
	var helper = Ember.Handlebars.helpers[helperName];

	Ember.assert("The " + helperName + " helper was not found", helper);

	return helper._rawFunction(parameter);
});
