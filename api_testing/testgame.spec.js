/// <reference types="cypress" />

var Tokens

describe('Play Game', function() {
    it('Test Get Token', function() {
       cy.request({
          method : 'POST',
          url : 'http://10.255.248.92/api/get_token',
          body: {
            "username": "test"
          },
          headers: {
             'content-type' : 'application/json'
          }
       }).then(function (response){
            Tokens = response.body.access_token
       })
    }),
    it('Test Start Game', function() {
      cy.request({
         method : 'GET',
         url : 'http://10.255.248.92/api/start_new_game',
         headers: {
            'content-type' : 'application/json',
            'Authorization' : "Bearer" + " " + Tokens
         }
      }).then(function (response){
         expect(response.body).to.eql({
            "message": "ready"
         })
            cy.log(response.body)
      })
   })
})