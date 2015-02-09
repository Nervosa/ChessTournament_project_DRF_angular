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
        var updateUser = function (changed_field, $data, participant_id, participant_data) {
            data_to_change = {};
            if ($data != participant_data) {
                data_to_change[changed_field] = $data;
                return $http.put('/api/participants/' + participant_id, data_to_change);
            }
        };

        var all_participants = function(){
            return $http({
                url: '/api/participants/',
                method: 'GET'
            })
        };

        var add_participant = function(name, surname, age, elo_rating){
            return $http({
                url: 'api/participants/',
                method: 'POST',
                data: { name: name, surname: surname, age: age, elo_rating: elo_rating }
            })
        };

        return {
            updateUser: updateUser,
            all_participants: all_participants,
            add_participant: add_participant
        };
    });