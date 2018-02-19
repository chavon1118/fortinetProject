$(document).ready(function() {
    // polling to check if database is updated
    setInterval(function () {
        $.ajax({
            url: 'checkupdate', //TODO: change to checkUpdate
            type: "GET",
            
            success: function (json) {
                if (json.data.length > 0) {
                    alert("new threats added"); // TODO: modify this to show new data
                }
            },
            
            error: function() {
                console.log("error")
            }
        });
    }, 10000);
});
