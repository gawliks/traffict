define(
    ['jquery', 'jqueryui', 'modernizr', 'foundation', 'knockout', 'django', 'vmfactory'],
    function (jquery, jqueryui, modernizr, foundation, ko, django, vmfactory) {
        var module = this;

        this.ApiViewModel = function() {
            this.confirmDelete = function(form) {
                if (confirm("Delete this API?")) return true;
                else return false;
            }
        }
        this.App = function() {
            ko.applyBindings(new module.ApiViewModel(), $('#subcontainer')[0]);
        }

        this.init = function() {
            new module.App()
        }

        this.init();
        return this;
});
