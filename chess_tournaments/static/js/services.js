angular.module('chess_app.services', [])
    .service('tournamentsService', function($http){
            var all_tournaments = function(){
                return $http({
                    url: '/api/tournaments',
                    method: 'GET'
                })
            };

            return {
                all_tournaments: all_tournaments
            }
        }

    )
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
    });
