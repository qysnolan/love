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

var commentApp = angular.module('commentApp', [
    'ngRoute',
    'ngCookies',
    'commentControllers',
    'commentFilters',
    'commentServices',
    'filters'
]);

commentApp.config(['$routeProvider',
    function($routeProvider) {
        $routeProvider.
            when('/', {
                templateUrl: '/static/app/views/comment_list.html',
                controller: 'CommentListCtrl'
            }).
            otherwise({
                redirectTo: '/'
            });
    }]);