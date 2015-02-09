angular.module('chess_app.controllers', [])
    .controller('ParticipantsController', ['$scope', 'participantsService', function($scope, participantsService){
            $scope.updateUser = participantsService.updateUser;
            $scope.not_admin = ($scope.user === "Anonymous") ? true : false;
            $scope.admin = ($scope.user === "Anonymous") ? false : true;
            participantsService.all_participants().success(function(data){
                $scope.all_participants = data;
            });
            $scope.addRow = function(){
                participantsService.add_participant($scope.name, $scope.surname, $scope.age, $scope.elo_rating)
                    .success(function(data){
                        console.log(data);
                        $scope.all_participants.push({'name': $scope.name,
                                                      'surname': $scope.surname,
                                                      'age': $scope.age,
                                                      'elo_rating': $scope.elo_rating});
                        $scope.name = undefined;
                        $scope.surname = undefined;
                        $scope.age = undefined;
                        $scope.elo_rating = undefined;
                    }).error(function(err){
                        console.log(err);
                    });
            };
        }]
    )
    .controller('showTournamentsCtrl', ['$scope', 'tournamentsService', function($scope, tournamentsService){
            tournamentsService.all_tournaments().success(function(data){
                $scope.all_tournaments = data;
            })
        }]);
