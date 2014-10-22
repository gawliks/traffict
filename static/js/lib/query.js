define(['jquery', 'knockout', 'vmfactory'], function($, ko, vmfactory) {
    var module = this;

    this.DialogFormWidget = function(options) {
        var self = this;

        this.dialogId = options.dialogId;
        this.fields = options.fields || {};
        this.url = options.url || null;

        this.init = function() {
            for (var f in this.fields) {
                $('#dialog-' + f).val(this.fields[f]);
                $('#dialog-' + f + '-error').toggle();
            };
            if (this.url) {
                $('#' + this.dialogId).load(
                    this.url,
                    function() {
                        //$('#' + this.dialogId).dialog();
                    }
                );
            }
        }

        this.init();
    }

    this.QueryViewModel = function(containerId, settings) {

        this.url = Django.url('api_manager:queries', settings.apiId);

        this.loadForm = function(data, event) {
            var elem = event.currentTarget;
            var id = $(elem).parent().parent().attr('id');
            var parts = id.split('-');
            new module.DialogFormWidget({
                dialogId: 'dialog',
                url: Django.url(
                    'api_manager:' + (parts.length == 1 ? 'new_query' : 'edit_query'),
                    parts
                )
            });
        }

        VMBase.call(this, containerId);
    }

    this.QueryViewModel.prototype = Object.create(VMBase.prototype);
    this.QueryViewModel.constructor = this.QueryViewModel;

    return this;
});
// define(['jquery', 'knockout', 'vmfactory', 'django'], function($, ko, vmfactory, django) {
//     var module = this;

//     this.DialogFormWidget = function(options) {
//         var self = this;

//         this.dialogId = options.dialogId;
//         this.fields = options.fields;

//         this.init = function() {
//             for (var f in this.fields) {
//                 $('#dialog-' + f).val(this.fields[f]);
//                 $('#dialog-' + f + '-error').toggle();
//             };
//             $('#' + this.dialogId).dialog();
//         }

//         this.init();
//     }

//     this.Query = function(options) {
//         var self = this;
//         this.id = ko.observable(options.id);
//         this.method = ko.observable(options.method);
//         this.body = ko.observable(options.body);
//         this.actionType = ko.computed(
//             function() {
//                 if (self.id() > 0) return "Edit";
//                 else return "Add";
//         });
//     };

//     this.QueryViewModel = function(containerId) {
//         var self = this;

//         this.url = '/query/';
//         this.template = 'query';
//         this.queries = ko.observableArray();

//         this.response = function(data) {
//             data.results.forEach(function(elem) {
//                 self.queries.push(new module.Query({
//                     id: elem.id,
//                     method: elem.method,
//                     body: elem.body
//                 }));
//             });
//             self.queries.push(new module.Query({
//                 id: 0, method: '', body: ''
//             }));
//         };

//         this.loadForm = function() {
//             new module.DialogFormWidget({
//                 dialogId: 'dialog',
//                 fields: {
//                     id: this.id(),
//                     method: this.method(),
//                     body: this.body()
//                 }
//             });
//         }

//         this.setQuery = function() {
//             var id = $('#dialog-id').val() || '';
//             if (id) id = id + '/';
//             $.ajax({
//                 url: '/query/' + id,
//                 type: "POST",
//                 dataType: "json",
//                 data: {
//                     method: $('#dialog-method').val(),
//                     body: $('#dialog-body').val()
//                 }
//             }).done(function(response) {
//                 $('#dialog').dialog("close");
//             }).fail(function(xhr, status, error) {
//                 console.log(xhr.responseText);
//                 console.log(status);
//                 console.log(error);
//                 var response = JSON.parse(xhr.responseText);
//                 for (var f in response) {
//                     $('#dialog-' + f + '-error').text(response[f]);
//                     $('#dialog-' + f + '-error').show();
//                 }
//             });
//         }

//         VMBase.call(this, containerId);

//         this.init = function () {
//         }
//         this.init();

//     }

//     this.QueryViewModel.prototype = Object.create(VMBase.prototype);
//     this.QueryViewModel.constructor = this.QueryViewModel;

//     return this;
// });