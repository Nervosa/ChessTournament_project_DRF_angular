angular.module('chess_app.services', ['ngResource'])
    .service('Tournaments', function TournamentsService($resource){
            return $resource('api/tournaments/:id', {});
        }

    )
    .service('participantsService', function ($http) {
        var update_participant = function (changed_field, $data, participant_id, participant_data) {
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

        var delete_participant = function(id){
            return $http({
                url: 'api/participants/' + id,
                method: 'DELETE'
            });
        };

        return {
            update_participant: update_participant,
            all_participants: all_participants,
            add_participant: add_participant,
            delete_participant: delete_participant
        };
    });