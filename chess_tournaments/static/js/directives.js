angular.module('chess_app.directives', [])
    .directive('focusThis', function($parse, $timeout){
        return {
            link: function(scope, element) {
                scope.$watch('trigger', function(){

                        $timeout(function () {
                            element[0].focus();
                        })
                })
            }
        }
    });
