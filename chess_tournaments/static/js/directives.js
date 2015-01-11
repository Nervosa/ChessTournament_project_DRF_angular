angular.module('chess_app.directives', [])
    .directive('focusThis', function($parse, $timeout, commonVarsService){
        return {

            link: function(scope, element) {
                scope.$watch('trigger', function(){
                    if (commonVarsService.shouldBeOpen === true){
                        $timeout(function () {
                            element[0].focus();
                        })
                    }
                })
            }
        }
    });
