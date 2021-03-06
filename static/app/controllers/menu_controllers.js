var menuControllers = angular.module('menuControllers', []);
var base_url = '/api/menus?type=';

menuControllers.controller('MenuListCtrl', function ($scope, $http) {
    var initiation = function() {
        $http.get(base_url+'1').success(function(data) {
            $scope.starters = data.results;
        });
        $http.get(base_url+'2').success(function(data) {
            $scope.entrees = data.results;
        });
        $http.get(base_url+'3').success(function(data) {
            $scope.desserts = data.results;
        });
        $scope.starter_name = starter_name;
        $scope.entree_name = entree_name;
        $scope.dessert_name = dessert_name;
        $scope.loading_data = loading_data;
    };

    initiation();
});
