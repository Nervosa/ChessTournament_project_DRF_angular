(function(){
    var chess_app = angular.module('chess_app', ['tableSort', 'xeditable', 'ngCookies', 'ui.bootstrap'], function ($interpolateProvider){
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
                $scope.all_participants = data.results;
            });
        });

    chess_app.controller('ModalDemoCtrl', function ($scope, $modal, $log) {

      $scope.items = ['item1', 'item2', 'item3'];

      $scope.open = function (size) {

        var modalInstance = $modal.open({
          templateUrl: 'myModalContent.html',
          controller: 'ModalInstanceCtrl',
          size: size,
          resolve: {
            items: function () {
              return $scope.items;
            }
          }
        });

        modalInstance.result.then(function (selectedItem) {
          $scope.selected = selectedItem;
        }, function () {
          $log.info('Modal dismissed at: ' + new Date());
        });
      };
    });

    chess_app.controller('ModalInstanceCtrl', function ($scope, $modalInstance, items) {

      $scope.items = items;
      $scope.selected = {
        item: $scope.items[0]
      };

      $scope.ok = function () {
        $modalInstance.close($scope.selected.item);
      };

      $scope.cancel = function () {
        $modalInstance.dismiss('cancel');
      };
    });
})();