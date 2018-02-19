$(document).ready(function() {

    $("#uploadfile").click(function(e){
        e.preventDefault();
        
        var data = new FormData($("form").get(0));
        var url = $("#threatfile")[0].attributes["data-url"].value;
        
        $.ajax({
            url: url,
            headers: {'X-CSRFToken': $.cookie('csrftoken')},
            type: "POST",
            data: data,
            processData: false,
            contentType: false,
            
            success: function (json) {
                if (json.data.length > 0) {
                    updateThreatTable(json.data);
                }
            },
            
            error: function (xhr, errmsg, err) {
                console.log(xhr.status + ": " + xhr.responseText);
            }
        });
    });

    // polling to check if database is updated
    setInterval(function () {
        $.ajax({
            url: 'checkupdate',
            type: "GET",
            
            success: function (json) {
                if (json.data.length > 0) {
                    updateThreatTable(json.data);
                }
            },
            
            error: function() {
                console.log("error")
            }
        });
    }, 10000); 
    // interval should be adjusted based on the probability of 
    // new data added through putting directly into media dir
});

function updateThreatTable(data) {
    if (!alert('new threats added')) {
        window.location.reload();
    }// TODO: modify this to show new data
}
