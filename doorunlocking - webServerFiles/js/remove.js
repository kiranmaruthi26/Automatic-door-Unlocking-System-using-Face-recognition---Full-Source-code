function removeImage(id) {
	var rm_btn = $('#rm_'+id);
	rm_btn.prop("value", "Removing...");
	rm_btn.prop('disabled', true);
	
    $.ajax({
        type:'POST',
        url:'../doorUnlocking/remove.php?id='+id,
        contentType: false,
        processData: false,
        success:function(result){
            //console.log("Success");
            console.log(result);
            if(result == "1"){
            	alert("Image Removed Successfully..!");
            	location.reload();
            }
            //$("#error").html(result);
            /*setTimeout(function(){
            },2000);*/
        },
        error:function (result) {
            console.log("Error");
        }

    });
}