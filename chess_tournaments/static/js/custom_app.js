(function(){
    var chess_app = angular.module('chess_app', ['tableSort', 'xeditable', 'ngCookies'], function ($interpolateProvider){
        $interpolateProvider.startSymbol("{[{");
        $interpolateProvider.endSymbol("}]}");
    });

    chess_app.run(function($http, $cookies){
        $http.defaults.headers.common['X-CSRFToken'] = $cookies['csrftoken'];
    });

    chess_app.service('participantsService', function ($http) {
        var updateUser = function ($data, participant_id, participant_name) {
            if ($data != participant_name) {
                return $http.put('/api/participants/' + participant_id, {name: $data});
            } else {
                alert('Nothing changed!!');
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
    });

    chess_app.controller('ParticipantsController',
        function($scope, participantsService){
            $scope.updateUser = participantsService.updateUser;
            participantsService.all_participants().success(function(data){
                $scope.all_participants = data;
            });
        });
})();