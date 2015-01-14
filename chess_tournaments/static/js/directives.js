angular.module('chess_app.directives', [])
    .directive('focusThis', function($timeout){
        return {
            link: function(scope, element, attrs){
                $timeout(function(){
                        element[0].focus();
                    }, 10)
            }
        }
    });