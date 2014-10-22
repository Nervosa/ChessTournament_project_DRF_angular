(function(){
    var chess_app = angular.module('chess_app', ['tableSort', 'xeditable', 'ngCookies'], function ($interpolateProvider){
        $interpolateProvider.startSymbol("{[{");
        $interpolateProvider.endSymbol("}]}");
    });

    //chess_app.run(function(editableOptions){
    //    editableOptions.theme = 'bs3';
    //});

    chess_app.run(function($http, $cookies){
        $http.defaults.headers.common['X-CSRFToken'] = $cookies['csrftoken'];
    });

    var textExtractor = function(node){
        return node.textContent;
    };

    chess_app.controller('ParticipantsController', function($scope, $http){
       $http.get('/api/participants/').success(function(data){
           $scope.all_participants = data;
       });

        $scope.updateUser = function($data, participant_id, participant_name){ //, participant_surname, participant_age, participant_elo

            if ($data != participant_name) {
                return $http.put('/api/participants/'+participant_id, {name: $data}); //, surname: participant_surname, age: participant_age, elo_rating: participant_elo
            } else {
                alert('Nothing changed!!');
            }
        }
    });
})();