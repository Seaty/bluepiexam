// <reference types="cypress" />

describe('ExamCheck', function () {
   it('Test Get Token', function () {
      cy.request({
         method: 'POST',
         url: 'http://localhost/api/get_token',
         body: {
            "username": "admin",
         },
         headers: {
            'content-type': 'application/json'
         }
      }).then(function (response) {
         expect(response.body).to.have.property("access_token")
         expect(response.body).to.have.property("token_type", "Bearer")
      })
   })
})