(function(){
    'use strict';

    angular
        .module('chess_app', ['tableSort', 'xeditable', 'ngCookies', 'LoginApp', 'ngRoute'], function ($interpolateProvider){
        $interpolateProvider.startSymbol("{[{");
        $interpolateProvider.endSymbol("}]}");
    })

        .run(function($http, $cookies){
        $http.defaults.headers.common['X-CSRFToken'] = $cookies['csrftoken'];
    })
        .config(function($routeProvider, $locationProvider){
            $routeProvider
                .when('/', {
                    //template: "<h1>MAIN ANG OLOLO {[{name}]}</h1>",
                    templateUrl: 'http://127.0.0.1:8000/main_ang.html',
                    controller: 'showSomethingCtrl'
                })
                .when('/tournaments', {
                    controller: 'showTournamentsCtrl'
                })
                .otherwise({
                    redirectTo: '/'
                });

            $locationProvider.html5Mode(true);
        })
        .service('participantsService', function ($http) {
        var updateUser = function ($data, participant_id, participant_name) {
            if ($data != participant_name) {
                return $http.put('/api/participants/' + participant_id, {name: $data});
            }
        };

        var all_participants = function(){
            return $http({
                url: '/api/participants',
                method: 'GET'
            })
        };

        return {
            updateUser: updateUser,
            all_participants: all_participants
        };
    })
        .controller('ParticipantsController', ['$scope', 'participantsService', function($scope, participantsService){
            $scope.updateUser = participantsService.updateUser;
            participantsService.all_participants().success(function(data){
                $scope.all_participants = data.results;
            });
        }]
    )
        .controller('mainPageCtrl', ['$scope', function($scope, $route, $routeParams, $location){
            $scope.$route = $route;
            $scope.$location = $location;
            $scope.$routeParams = $routeParams;

        }])
        .controller('showSomethingCtrl', ['$scope', function($scope){
            $scope.name = ($scope.user) ? ($scope.user) : ('Anonymous');
        }])
        .controller('showTournamentsCtrl', ['$scope', '$http', function($scope, $http){
            $http.get('/tournaments/');
        }])
    ;

})();