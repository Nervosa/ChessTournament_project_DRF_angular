angular.module('chess_app.directives', [])
    .directive('focusThis', function($timeout){
        return {
            link: function(scope, element, attrs){
                $timeout(function(){
                        error_element = document.querySelector("#error_message");
                        angular.element(error_element).hide();
                        element[0].focus();
                    }, 10)
            }
        }
    });