// <reference types="cypress" />

describe('DFMAPI', function() {
    it('Test LoginDTC', function() {
       cy.request({
          method : 'POST',
          url : 'http://www.dtcgps.com:8097/login_mb',
          body: {
            "user": "devadmin",
	        "pass": "i516j5l5p4w5"
          },
          headers: {
             'content-type' : 'application/json'
          }
       }).then(function (response){
          
            expect(response.body).to.include({
                "user_id": "UEVO-00001",
                "user_login": "devadmin",
                "user_name": "dev admin"       
            })
       })
    }),
    it('Test get_station_type_mb', function() {
        cy.request({
           method : 'POST',
           url : 'http://www.dtcgps.com:8097/get_station_type_mb',
           body: {
            "ssid": "devadmin"
           },
           headers: {
              'content-type' : 'application/json'
           }
        }).then(function (response){
           
             expect(response.body[0]).to.include({
               "response": "ok",
                "msg": "ok"
             })
        })
     }),
     it('Test get_station_mb', function() {
        cy.request({
           method : 'POST',
           url : 'http://www.dtcgps.com:8097/get_station_mb',
           body: {
            "ssid": "devadmin"
           },
           headers: {
              'content-type' : 'application/json'
           }
        }).then(function (response){
           
             expect(response.body[0]).to.include({
                "response": "ok",
                "msg": "ok"        
             })
        })
     }),
     it('Test get_group_mb', function() {
        cy.request({
           method : 'POST',
           url : 'http://www.dtcgps.com:8097/get_group_mb',
           body: {
            "ssid": "devadmin"
           },
           headers: {
              'content-type' : 'application/json'
           }
        }).then(function (response){
           
             expect(response.body[0]).to.include({
                "response": "ok",
                "msg": "ok"        
             })
        })
     }),
     it('Test get_truck_mb', function() {
        cy.request({
           method : 'POST',
           url : 'http://www.dtcgps.com:8097/get_truck_mb',
           body: {
                "ssid": "devadmin",
	            "group": "all"
           },
           headers: {
              'content-type' : 'application/json'
           }
        }).then(function (response){
           
             expect(response.body[0]).to.include({
                "response": "ok",
                "msg": "ok"        
             })
        })
     }),
     it('Test realtime_mb', function() {
        cy.request({
           method : 'POST',
           url : 'http://www.dtcgps.com:8097/realtime_mb',
           body: {
            "ssid": "devadmin",
            "group_id": "all",
            "mode": "all",
            "post_lang": "th",
            "lastupdates": ""
           },
           headers: {
              'content-type' : 'application/json'
           }
        }).then(function (response){
           
             expect(response.body[0]).to.include({
                "response": "ok",
                "msg": "ok"        
             })
        })
     }),
     it('Test history_mb', function() {
        cy.request({
           method : 'POST',
           url : 'http://www.dtcgps.com:8097/history_mb',
           body: {
            "ssid": "devadmin",
	        "blackboxid": "102651318431",
	        "start": "2020-11-23 00:00",
	        "end": "2020-11-23 23:59"
           },
           headers: {
              'content-type' : 'application/json'
           }
        }).then(function (response){
           
             expect(response.body[0]).to.include({
                "response": "ok"     
             })
        })
     }),
     it('Test notification_mb', function() {
        cy.request({
           method : 'POST',
           url : 'http://www.dtcgps.com:8097/notification_mb',
           body: {
            "ssid": "devadmin"
           },
           headers: {
              'content-type' : 'application/json'
           }
        }).then(function (response){
           
             expect(response.body[0]).to.include({
                "response": "ok",
                "msg": "ok"        
             })
        })
     }),
     it('Test get_setting_notify', function() {
        cy.request({
           method : 'POST',
           url : 'http://www.dtcgps.com:8097/get_setting_notify',
           body: {
            "ssid": "devadmin"
           },
           headers: {
              'content-type' : 'application/json'
           }
        }).then(function (response){
           
             expect(response.body[0]).to.include({
                "response": "ok"       
             })
        })
     }),
     it('Test report_daily', function() {
        cy.request({
           method : 'POST',
           url : 'http://www.dtcgps.com:8097/report_daily',
           body: {
            "ssid": "388AAE58-C203-49D3-8FA2-1C56F1786680",
	        "blackbox_id": "102651318431",
	        "start_date": "2020-11-23 00:00",
	        "end_date": "2020-11-23 23:59",
	        "lang": "th"
           },
           headers: {
              'content-type' : 'application/json'
           }
        }).then(function (response){
           
             expect(response.body[0]).to.include({
                "response": "ok",
                "msg": "ok" 
             })
        })
     }),
     it('Test report_trip', function() {
        cy.request({
           method : 'POST',
           url : 'http://www.dtcgps.com:8097/report_trip',
           body: {
            "ssid": "388AAE58-C203-49D3-8FA2-1C56F1786680",
	        "blackbox_id": "102651318431",
	        "start_date": "2020-11-23 00:00",
	        "end_date": "2020-11-23 23:59",
	        "lang": "th"
           },
           headers: {
              'content-type' : 'application/json'
           }
        }).then(function (response){
           
             expect(response.body[0]).to.include({
                "response": "ok" ,
                "msg": "ok"  
             })
        })
     }),
     it('Test report_stop', function() {
        cy.request({
           method : 'POST',
           url : 'http://www.dtcgps.com:8097/report_stop',
           body: {
            "ssid": "388AAE58-C203-49D3-8FA2-1C56F1786680",
	        "blackbox_id": "102651318431",
	        "start_date": "2020-11-23 00:00",
	        "end_date": "2020-11-23 23:59",
	        "lang": "th",
            "time": "0"
           },
           headers: {
              'content-type' : 'application/json'
           }
        }).then(function (response){
           
             expect(response.body[0]).to.include({
                "response": "ok" ,
                "msg": "ok"   
             })
        })
     }),
     it('Test report_idle', function() {
        cy.request({
           method : 'POST',
           url : 'http://www.dtcgps.com:8097/report_idle',
           body: {
            "ssid": "388AAE58-C203-49D3-8FA2-1C56F1786680",
	        "blackbox_id": "102651318431",
	        "start_date": "2020-11-23 00:00",
	        "end_date": "2020-11-23 23:59",
	        "lang": "th",
            "time": "0"
           },
           headers: {
              'content-type' : 'application/json'
           }
        }).then(function (response){
           
             expect(response.body[0]).to.include({
                "response": "ok" ,
                "msg": "ok"  
             })
        })
     }),
     it('Test report_over_speed', function() {
        cy.request({
           method : 'POST',
           url : 'http://www.dtcgps.com:8097/report_over_speed',
           body: {
            "ssid": "388AAE58-C203-49D3-8FA2-1C56F1786680",
	        "blackbox_id": "102651318431",
	        "start_date": "2020-11-23 00:00",
	        "end_date": "2020-11-23 23:59",
	        "lang": "th",
            "time": "0"
           },
           headers: {
              'content-type' : 'application/json'
           }
        }).then(function (response){
           
             expect(response.body[0]).to.include({
                "response": "ok"   ,
                "msg": "ok"  
             })
        })
     }),
     it('Test report_gpslost', function() {
        cy.request({
           method : 'POST',
           url : 'http://www.dtcgps.com:8097/report_gpslost',
           body: {
            "ssid": "388AAE58-C203-49D3-8FA2-1C56F1786680",
	        "blackbox_id": "102651318431",
	        "start_date": "2020-11-23 00:00",
	        "end_date": "2020-11-23 23:59",
	        "lang": "th"
           },
           headers: {
              'content-type' : 'application/json'
           }
        }).then(function (response){
           
             expect(response.body[0]).to.include({
                "response": "ok",
                "msg": "ok" 
             })
        })
     }),
     it('Test report_pto', function() {
        cy.request({
           method : 'POST',
           url : 'http://www.dtcgps.com:8097/report_pto',
           body: {
            "ssid": "388AAE58-C203-49D3-8FA2-1C56F1786680",
	        "blackbox_id": "102651318431",
	        "start_date": "2020-11-23 00:00",
	        "end_date": "2020-11-23 23:59",
	        "lang": "th"
           },
           headers: {
              'content-type' : 'application/json'
           }
        }).then(function (response){
           
             expect(response.body[0]).to.include({
                "response": "ok"   ,
                "msg": "ok" 
             })
        })
     }),
     it('Test report_hd', function() {
        cy.request({
           method : 'POST',
           url : 'http://www.dtcgps.com:8097/report_hd',
           body: {
            "ssid": "388AAE58-C203-49D3-8FA2-1C56F1786680",
	        "blackbox_id": "102651318431",
	        "start_date": "2020-11-23 00:00",
	        "end_date": "2020-11-23 23:59",
	        "lang": "th"
           },
           headers: {
              'content-type' : 'application/json'
           }
        }).then(function (response){
           
             expect(response.body[0]).to.include({
                "response": "ok"  ,
                "msg": "ok" 
             })
        })
     }),
     it('Test report_ha', function() {
        cy.request({
           method : 'POST',
           url : 'http://www.dtcgps.com:8097/report_ha',
           body: {
            "ssid": "388AAE58-C203-49D3-8FA2-1C56F1786680",
	        "blackbox_id": "102651318431",
	        "start_date": "2020-11-23 00:00",
	        "end_date": "2020-11-23 23:59",
	        "lang": "th"
           },
           headers: {
              'content-type' : 'application/json'
           }
        }).then(function (response){
           
             expect(response.body[0]).to.include({
                "response": "ok"  ,
                "msg": "ok" 
             })
        })
     }),
     it('Test report_tostation', function() {
        cy.request({
           method : 'POST',
           url : 'http://www.dtcgps.com:8097/report_tostation',
           body: {
            "ssid": "388AAE58-C203-49D3-8FA2-1C56F1786680",
	        "blackbox_id": "102651318431",
	        "start_date": "2020-11-23 00:00",
	        "end_date": "2020-11-23 23:59",
	        "lang": "th"
           },
           headers: {
              'content-type' : 'application/json'
           }
        }).then(function (response){
           
             expect(response.body[0]).to.include({
                "response": "ok"  ,
                "msg": "ok" 
             })
        })
     }),
     it('Test report_instation', function() {
        cy.request({
           method : 'POST',
           url : 'http://www.dtcgps.com:8097/report_instation',
           body: {
            "ssid": "388AAE58-C203-49D3-8FA2-1C56F1786680",
	        "blackbox_id": "102651318431",
            "stationtype_id": "all",
	        "station_id": "all",
	        "start_date": "2020-11-23 00:00",
	        "end_date": "2020-11-23 23:59",
	        "lang": "th"
           },
           headers: {
              'content-type' : 'application/json'
           }
        }).then(function (response){
           
             expect(response.body[0]).to.include({
                "response": "ok" ,
                "msg": "ok" 
             })
        })
     }),
     it('Test master_notify', function() {
        cy.request({
           method : 'POST',
           url : 'http://www.dtcgps.com:8097/master_notify',
           body: {
            "ssid":"devadmin"
           },
           headers: {
              'content-type' : 'application/json'
           }
        }).then(function (response){
           
             expect(response.body[0]).to.include({
                "response": "ok" ,
                "msg": "ok" 
             })
        })
     }),
     it('Test get_employee_mb', function() {
        cy.request({
           method : 'POST',
           url : 'http://www.dtcgps.com:8097/get_employee_mb',
           body: {
            "ssid":"devadmin"
           },
           headers: {
              'content-type' : 'application/json'
           }
        }).then(function (response){
           
             expect(response.body[0]).to.include({
                "response": "ok",
                 "msg": "ok"     
             })
        })
     }),
     it('Test report_grahp_fuel', function() {
        cy.request({
           method : 'POST',
           url : 'http://www.dtcgps.com:8097/report_grahp_fuel',
           body: {
            "ssid": "devadmin",
	        "blackbox_id": "102651318431",
	        "start": "2020-11-23 00:00",
	        "end": "2020-11-23 23:59"
           },
           headers: {
              'content-type' : 'application/json'
           }
        }).then(function (response){
           
             expect(response.body[0]).to.include({
                "response": "ok" 
             })
        })
     })
})