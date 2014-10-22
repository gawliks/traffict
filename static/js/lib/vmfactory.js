define(['jquery', 'knockout', 'django'], function($, ko, django) {

    this.NotImplementedException = function(msg) {
        this.message = msg;
    }

    this.VMFactory = function(options) {
        var self = this;

        this.module = options.module;
        this.viewModel = options.viewModel ? options.viewModel :
            this.module.charAt(0).toUpperCase() + this.module.slice(1) + 'ViewModel';
        this.container = options.container ? options.container :
            this.module + '-container';
        this.restful = options.restful || false;
        this.vmSettings = options.vmSettings;

        this.init = function() {
            require([this.module], function (m) {
                var obj = new this[self.viewModel](
                    self.container, self.vmSettings
                );
            });
        };
        this.init();
    }

    this.VMBase = function(containerId) {
        var self = this;

        this.containerId = containerId;
        this.container = $('#' + containerId);

        this.init();
    }

    this.VMBase.prototype.init = function() {
        var self = this;
        if (this.restful) {
            $.getJSON(this.url, function(data) {
                self.container.load(
                    Django.url('api_manager:template', self.template),
                    function() {
                        ko.applyBindings(self, self.container[0]);
                        self.response(data);
                    });
            });
        }
        else {
            this.container.load(
                this.url,
                function() {
                    ko.applyBindings(self, self.container[0]);
                    self.response();
                }
            );
        }
    }

    this.VMBase.prototype.response = function(data) {}

    return this;
});