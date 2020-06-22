
$('.bn').click(function(){
    $('.collapse').collapse('hide');
});
/*$('#reservation').submit(function(event){
    event.preventDefault()
    
});*/
function branchchange(){
    var id = document.all('branch').value;
    if (id!=''){
        $.ajax({
            url: 'select/'+id,
            method:"GET",
            success:function(data){
                let rows =  '';
                data.halls.forEach(hall => {
                rows += 
                '<option value="'+hall.id+'">'+hall.title+'</option>'
                ;
            });
            $('#hall').empty();
            $('#hall').append('<option value="">--- Hall ---</option>'+rows);

            }
        })
    }
    else{
        $('#hall').empty();
        $('#hall').append('<option value="">--- Hall ---</option>');
    }
}
$('.form-meal').submit(function(e){
    e.preventDefault()
})
$("input[type='radio']").click(function(){
    bill();
});
$('#hall').change(function(){
    bill();
    check();
});
$('#size').keyup(function(){
    bill();
});

function bill(){
    var meal = $("input[name='meal']:checked").val();
    var hall = $('#hall').val();
    var size = $('#size').val();
    var mealcharges = $('#mealcharges'+meal).val();
    
    if (meal!=undefined &&  hall!='' && size!='')
    {
        $.ajax({
            url: 'hall_charges/'+meal,
            method:"GET",
            success:function(data){
               var total = (parseFloat(mealcharges)+parseFloat(data))*parseFloat(size);
               $('#estimated').empty();
               $('#charges').val(total);
               $('#estimated').append('Estimated Charges: '+total+' Rs.');
            }
        })
    }
}
$('#date').focusout(function(){
    var date = $('#date').val();
    if (date!=''){
        var d = new Date();
        var mm = d.getMonth()+1;
        if (d.getDate()<10){
            var dateNow = d.getFullYear()+'-'+mm+'-0'+d.getDate();
        }
        if (mm<10){
            var dateNow = d.getFullYear()+'-0'+mm+'-'+d.getDate();
        }
        if (date<dateNow){
            alert("Incorrect Date, Date has Passed")
            $('#date').val('');
        }
        check();
    }
})
$('#time').change(function(){
    check();    
});
function check(){
    var date = $('#date').val();
    var time = $('#time').val();
    var hal = $('#hall').val();
    if (date!='' &&  time!='' && hal!='')
    {
        $.ajax({
            url: 'check/',
            method:"GET",
            success:function(data){
                console.log(data)
               var d='';
               var c=0;
                data.rhalls.forEach(rhall => {
                    if (rhall.hall_id==hal){
                        for (i = 0;i<rhall.Date.length;i++){
                            if (rhall.Date[i]!='T'){
                                d+=rhall.Date[i];
                            }
                            else{
                                break
                            }
                        }
                        if(d==date){
                            if (rhall.Time==time){
                                c=1;
                            }
                        }
                    }
                    d='';
                });
                if (c==1){
                alert("Hall is Already Booked At This Time")
                $('#time').val("");
                }
            }
        })
    }
} 