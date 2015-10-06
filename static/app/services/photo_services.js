/* Services */

var photoServices = angular.module('photoServices', ['ngResource']);

photoServices.factory('Photo', ['$resource',
    function($resource){
        return $resource('api/photos/:photoId', {}, {
            query: {method:'GET', params:{photoId:'photos'}, isArray:true}
        });
    }]);

angular.module('filters', []).
    filter('truncate', function () {
        return function (text, length) {
            if(text==undefined)
                return text;
            var end = "...";
            if (text.length <= length || text.length - end.length <= length) {
                return text;
            }
            else {
                return String(text).substring(0, length-end.length) + end;
            }
        };
    });