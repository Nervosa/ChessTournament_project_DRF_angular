login_app = angular.module('LoginApp', ['ui.bootstrap', 'ngResource']).config(['$httpProvider', function($httpProvider){
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
}]).factory('api', function($resource){
    function add_auth_header(data, headersGetter){
        var headers = headersGetter();
        headers['Authorization'] = ('Basic ' + btoa(data.username + ':' + data.password));
    }
    return {
        auth: $resource('/api/auth\\/', {}, {
            login: {method: 'POST', transformRequest: add_auth_header},
            logout: {method: 'DELETE'}
        }),
        users: $resource('/api/users\\/', {}, {
            create: {method: 'POST'}
        })
    };
}).controller('authController', function($scope, api){


    $scope.getCredentials = function(){
        return {username: $scope.username, password: $scope.password};
    };

    $scope.login = function(){
        $('#id_auth_form input').checkAndTriggerAutoFillEvent();
        $scope.locationToReturn = window.location.href;
        api.auth.login($scope.getCredentials()).$promise.
        then(function(data){
            $scope.user = data.username; //when got valid username and password
            $scope.ok();
            window.location.replace($scope.locationToReturn);
        }).
        catch(function(data){
            alert(data.data.detail);    //when got incorrect username and password
        });
    };
});

login_app.controller('ModalDemoCtrl', function ($scope, $modal, $log, api) {

      $scope.open = function (size) {

        var modalInstance = $modal.open({
          templateUrl: 'myModalContent.html',
          controller: 'ModalInstanceCtrl',
          size: size
        });

        modalInstance.result.then(function () {
          $log.info('Modal dismissed at: ' + new Date());
        });
      };

    $scope.log_out = function(){
        $scope.locationToReturn = window.location.href;
        api.auth.logout(function(){
            $scope.user = undefined;
        })
        window.location.replace($scope.locationToReturn);
    };
    });

login_app.controller('ModalInstanceCtrl', function ($scope, $modalInstance) {

      $scope.ok = function () {
        $modalInstance.close();
      };

      $scope.cancel = function () {
        $modalInstance.dismiss('cancel');
      };
    });