(function(){
    'use strict';

    angular
        .module('chess_app', ['tableSort',
                              'xeditable',
                              'ngCookies',
                              'LoginApp',
                              'ui.router',
                              'chess_app.services',
                              'chess_app.directives',
                              'chess_app.controllers'],
                              function ($interpolateProvider){
                                $interpolateProvider.startSymbol("{[{");
                                $interpolateProvider.endSymbol("}]}");
                              })

        .run(
            function($http, $cookies){
                $http.defaults.headers.common['X-CSRFToken'] = $cookies['csrftoken'];
            })
        .config(function($stateProvider, $urlRouterProvider, $locationProvider){

            $urlRouterProvider.otherwise("/");

            $stateProvider
                .state({
                    name: 'land',
                    url: "/",
                    templateUrl: "/partials/main_ang.html"
                    //controller: 'showSomethingCtrl'
                })
                .state({
                    name: 'tournaments',
                    url: "/tournaments/",
                    templateUrl: '/partials/tournaments_list_ang.html',
                    controller: 'showTournamentsCtrl'
                })
                .state({
                    name: 'participants',
                    url: "/participants/",
                    templateUrl: 'partials/participants_list.html',
                    controller: 'showParticipantsController'
                });
            $locationProvider.html5Mode(true);
        })
})();