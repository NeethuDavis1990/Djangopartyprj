jQuery(document).ready(function(){

   jQuery('.select2').select2({
               width:'350px'})
                              

   jQuery('.datepicker').datepicker()

   

    jQuery('#id_Category').change(function(){


        var category=jQuery("#id_Category").val()

        jQuery.ajax({
            type: "GET",
            url:"../Getfoodlistbasedoncategoryusingajax",
            contents: "application/json; charset=utf-8",
            dataType: "json",
            data: { "argcategory": category},
            success: function (response) {
                console.log(response)

                jQuery('#id_Foodlist').empty().append('<option selected="selected" value="">Please select Food items</option>');
                jQuery.each(response, function (i, item) {

                    jQuery('#id_Foodlist').append(`<option value="${item.value}">${item.text}</option>`);


                });


            }
        });


    });



    jQuery('#id_Partyname').blur(function(){

        var partyname=jQuery(this).val();
        
        jQuery.ajax({
            type: "GET",
            url:"Partynameduplicatevalidation",
            contents: "application/json; charset=utf-8",
            dataType: "json",
            data: { "argpartyname": partyname},
            success: function (response) {
                console.log(response)                      
            
            }

                        
            
        });

    });

      jQuery('#id_Time').blur(function(){
          
        var newtime=jQuery(this).val();
        var newdate=jQuery('#id_Date').val()
        var newvenue=jQuery('#id_Venu').val()

        jQuery.ajax({
            type: "GET",
            url:"Repeatedvenudateandtimeresponsefn",
            contents: "application/json; charset=utf-8",
            dataType: "json",
            data: { "argnewtime": newtime,"argnewdate":newdate,"argnewvenue":newvenue},
            success: function (response) {
                console.log(response)                      
            
            }

                        
            
        });
      







      })

      jQuery('#id_Gametype').blur(function(){



        
      })
})
