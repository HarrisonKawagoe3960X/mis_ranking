$(document).ready(function() {

  $('#btn').on('click', function() {
    $.ajax({
               'url':'/getinf?id='+$("#gameid").val(),
               'type':'GET',
               'success':function(response){
                     $('#rankinf').text(JSON.stringify(response));
               },
           });
  });

  $('#csv').on('click', function() {
    console.log(114514);
    window.location.href='/getcsv?id='+$("#gameid").val();
    return false;
  });

  $('#submit_form').submit(function() {
    $.ajax({
               'url':$('form#submit_form').attr('action'),
               'type':'POST',
               'data':$('form#submit_form').serialize(),
               'dataType':'json',
               'success':function(response){
                     $('#gameid').text("Id:"+response.result);
               },
           });
    return false;
    });
});
