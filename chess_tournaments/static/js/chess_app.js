(function(){
    'use strict';

    angular
        .module('chess_app', ['tableSort', 'xeditable', 'ngCookies', 'LoginApp', 'ui.router'], function ($interpolateProvider){
        $interpolateProvider.startSymbol("{[{");
        $interpolateProvider.endSymbol("}]}");
    })

        .run(function($http, $cookies){
        $http.defaults.headers.common['X-CSRFToken'] = $cookies['csrftoken'];
    })
        .config(function($stateProvider, $urlRouterProvider){
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
                    controller: 'showSomethingCtrl'
                })
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
        .controller('showSomethingCtrl', ['$scope', function($scope){
            $scope.visitor = {name: ''};
            $scope.visitor.name = ($scope.user) ? ($scope.user) : "Anonymous";
        }])
        .controller('showTournamentsCtrl', ['$scope', '$http', function($scope, $http){
            $http.get('/tournaments/');
        }])
    ;

})();