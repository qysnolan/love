var photoControllers = angular.module('photoControllers', []);
var base_url = '/api/photos';

photoControllers.controller('PhotoListCtrl', function ($scope, $http) {
    var initiation = function() {
        $http.get(base_url).success(function(data) {
            $scope.photos = data.results;
            $scope.count = data.count;
            $scope.previous = data.previous;
            $scope.next = data.next;
            $scope.totalPages = Math.ceil($scope.count/25);
            $scope.currentPage = 1;
            $scope.firstEntry = 25 * ($scope.currentPage - 1) + 1;
            $scope.lastEntry = $scope.firstEntry + 24 > $scope.count
                ? $scope.count : $scope.firstEntry + 24;
            var pages = [];
            for(var i=0; i<$scope.totalPages; i++)
                pages[i] = {"number": i+1};
            $scope.pages = pages;
            $scope.pageNumber = $scope.currentPage;
            $scope.base_url = base_url;
            checkDisable();
        });
        $scope.firstDisable = true;
        $scope.lastDisable = true;
        $scope.nextDisable = false;
        $scope.previousDisable = false;
        $scope.allDataLoaded = false;
        $scope.allDataLoading = false;
        $scope.query = null;
    };

    initiation();

    var checkDisable = function() {
        $scope.previous==undefined
            ? $scope.previousDisable = true : $scope.previousDisable = false;
        $scope.next==undefined
            ? $scope.nextDisable = true : $scope.nextDisable = false;
        $scope.currentPage==1
            ? $scope.firstDisable = true : $scope.firstDisable = false;
        $scope.totalPages==$scope.currentPage
            ? $scope.lastDisable = true : $scope.lastDisable = false;
    };

    $scope.loadPhotos = function(url) {
        $http.get(url).success(function(data) {
            var data1 = $scope.photos;
            var data2 = data.results;
            $scope.photos = $.merge(data1, data2);
            $scope.previous = data.previous;
            $scope.next = data.next;
            $scope.currentPage ++;
            $scope.pageNumber = $scope.currentPage;
            $scope.firstEntry = 25 * ($scope.currentPage - 1) + 1;
            $scope.lastEntry = $scope.firstEntry + 24 > $scope.count
                ? $scope.count : $scope.firstEntry + 24;
            $scope.query = null;
            if(data.next==null)
                $scope.allDataLoaded = true;
        });
    };
});
