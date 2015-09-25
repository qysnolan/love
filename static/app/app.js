var photoApp = angular.module('photoApp', [
    'ngRoute',
    'ngCookies',
    'photoControllers',
    'photoFilters',
    'photoServices',
    'filters'
]);

photoApp.config(['$routeProvider',
    function($routeProvider) {
        $routeProvider.
            when('/', {
                templateUrl: '/static/app/views/photo_list.html',
                controller: 'PhotoListCtrl'
            }).
            otherwise({
                redirectTo: '/'
            });
    }]);
