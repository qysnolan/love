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

var menuApp = angular.module('menuApp', [
    'ngRoute',
    'ngCookies',
    'menuControllers',
    'menuFilters',
    'menuServices',
    'filters'
]);

menuApp.config(['$routeProvider',
    function($routeProvider) {
        $routeProvider.
            when('/', {
                templateUrl: '/static/app/views/menu_list.html',
                controller: 'MenuListCtrl'
            }).
            otherwise({
                redirectTo: '/'
            });
    }]);