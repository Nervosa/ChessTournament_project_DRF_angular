(function(){
    'use strict';

    angular
        .module('chess_app', ['tableSort',
                              'xeditable',
                              'ngCookies',
                              'LoginApp',
                              'ui.router',
                              'chess_app.services',
                              'chess_app.controllers'],
                              function ($interpolateProvider){
                                $interpolateProvider.startSymbol("{[{");
                                $interpolateProvider.endSymbol("}]}");
                              })

        .run(
            function($http, $cookies){
                $http.defaults.headers.common['X-CSRFToken'] = $cookies['csrftoken'];
            })
        .config(function($stateProvider, $urlRouterProvider, $locationProvider){

            $urlRouterProvider.otherwise("/");

            $stateProvider
                .state({
                    name: 'land',
                    url: "/",
                    templateUrl: "main_ang.html",
                    controller: 'showSomethingCtrl'
                })
                .state({
                    name: 'tournaments',
                    url: "tournaments/",
                    templateUrl: 'tournaments_list_ang.html',
                    controller: 'showTournamentsCtrl'
                });
            $locationProvider.html5Mode(true);
        })
        .controller('showSomethingCtrl', ['$scope', function($scope){
            $scope.just_a_var = 'I\'m a var';
        }]);
})();