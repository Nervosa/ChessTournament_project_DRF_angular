angular.module('chess_app.controllers', [])
    .controller('ParticipantsController', ['$scope', 'participantsService', function($scope, participantsService){
            $scope.updateUser = participantsService.updateUser;
            $scope.not_admin = ($scope.user === "Anonymous") ? true : false;
            $scope.admin = ($scope.user === "Anonymous") ? false : true;
            participantsService.all_participants().success(function(data){
                $scope.all_participants = data;
            });
        }]
    )
    .controller('showTournamentsCtrl', ['$scope', 'tournamentsService', function($scope, tournamentsService){
            tournamentsService.all_tournaments().success(function(data){
                $scope.all_tournaments = data;
            })
        }]);
