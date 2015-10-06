/* Services */

var commentServices = angular.module('commentServices', ['ngResource']);

commentServices.factory('Comment', ['$resource',
    function($resource){
        return $resource('api/comments/:commentId', {}, {
            query: {method:'GET', params:{commentId:'comments'}, isArray:true}
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