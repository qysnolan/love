var menuServices = angular.module('menuServices', ['ngResource']);

menuServices.factory('Menu', ['$resource',
    function($resource){
        return $resource('api/menu/:menuId', {}, {
            query: {method:'GET', params:{menuId:'menus'}, isArray:true}
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