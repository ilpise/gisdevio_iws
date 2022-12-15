
    const data = document.currentScript.dataset;

    $("#go").click(function (e) {
        // preventing from page reload and default actions
        e.preventDefault();

        $("#progressModal").modal("show");
        var threddsUrl = $("#id_url").val()
        // make POST ajax call
        $.ajax({
            type: 'POST',
            url: data.url, // parse_catalog route from thredds
            data: {"url": threddsUrl},
            success: function (response) {
                var obj = JSON.parse(response)
                console.log(obj)
                var out = ''
                $.each(obj, function( index, value ) {
                    out += '<div class="form-group">'+
                            '<input type="button" class="btn btn-primary follow" data-pid="'+index+'" data-href="'+value.href+'" data-name="'+value.name+'" value="'+value.title+'" />'+
                            '<div id="'+index+'" class="form-group">'+
                            '</div>'+
                           '</div>'
                });
                $('#subcoll').html(out);
                $("#progressModal").modal("hide");
            },
            error: function (response) {
                // alert the error if any error occured
                $("#progressModal").modal("hide");
//                alert(response["responseJSON"]["error"]);
            },
            complete: function (response) {
                console.log('COMPLETE')
                // Attach follow functionalities
                followUrl()
            }
        })
    })

//    function

    function followUrl (){
        console.log('FOLLOW ATTACHED')
        $('.follow').click(function(){
            $("#progressModal").modal("show");
            //  console.log($(this))
            //  console.log($(this).data("href"));
            $.ajax({
                type: 'POST',
                url: data.follow,
//                data: $(this).data("href"),
                data: {'getdata': $(this).data("href"), 'pid':$(this).data("pid")},
                success: function (response) {
                    console.log(response)
                    var out = ''
                    $.each(response.data, function( index, value ) {
                        console.log(value)
                        console.log(value.hasOwnProperty('catalog'))
                        if (value.hasOwnProperty('catalog')) {
                            console.log('ENTERED')
                            out += '<div class="form-group">'+
                                   '<input type="button" class="btn btn-primary follow" data-pid="'+response.pid+'_'+index+'" data-href="'+value.catalog.href+'" data-name="'+value.catalog.name+'" value="'+value.catalog.title+'" />'+
                                   '<div id="'+response.pid+'_'+index+'" class="form-group">'+
                                   '</div>'+
                                   '</div>'
                        }
                        if (value.hasOwnProperty('datasets')) {
                            var table = '<table class="table table-hover table-condensed">'+
                            '<thead><tr><td>Service</td><td>URL</td><td>Save</td></tr></thead><tbody>';
                            $.each(value.datasets.access_urls, function( i, val ) {
                                if(i == "WMS"){
                                    table += '<tr><td>'+i+'</td><td>'+val+'</td><td><input type="button" class="btn btn-primary wms-resource" data-href="'+val+'" value="SAVE SERVICE" /></td></tr>'
                                } else {
                                    table += '<tr><td>'+i+'</td><td><a href="'+val+'">'+val+'</a></td><td></td></tr>'
                                }
                            });
                            table += '</tbody></table>';

                            out += '<div class="form-group">'+
//                                   '<input type="button" class="btn btn-primary" data-pid="'+response.pid+'_'+index+'" data-name="'+value.datasets.name+'" value="'+value.datasets.name+'" />'+
                                   '<div><h3>'+value.datasets.name+'</h3></div>'+
                                   table+
                                   '</div>'
                        }
                    });
                    $('#'+response.pid).html(out);
                },
                error: function (response) {
//                    console.log(response)
                    $("#progressModal").modal("hide");
                    alert(response["responseJSON"]["error"]);
                },
                complete: function (response) {
                    console.log('COMPLETE')
                    // Attach follow functionalities
                    followUrl()
                    $('.wms-resource').click(function(){
                //        $(this)
                        console.log($(this).data("href"));
                        var url = $(this).data("href")
                             $.ajax({
                                type: 'POST',
                                url: 'http://localhost:8000/thredds/register_service_wms/',
                                data: {url: url,
                                       type:'WMS',
                                       },
                                success: function (response, textStatus, jqXHR) {
                                    console.log(response)
                                    window.location.href = 'http://localhost:8000'+response;
                                },
                                error: function (response) {
                                    console.log(response)
                                }
                            })
                    })
                    $("#progressModal").modal("hide");
                }

            })
        });
    }



    $('#test').click(function(){
//        $(this)
        console.log($(this).data("href"));
        var url = $(this).data("href")
             $.ajax({
                type: 'POST',
//                method: 'POST',
                url: 'http://localhost:8000/thredds/register_service_wms/',
//                data: $(this).data("href"),
                data: {url: url,
                       type:'WMS',
//                       action: 'post'
                       },
                success: function (response, textStatus, jqXHR) {
                    console.log(textStatus)
                    console.log(jqXHR)
                    console.log(jqXHR.url)
                    console.log(jqXHR.getAllResponseHeaders())
//                    console.log(jqXHR.getResponseHeader(e))
                    console.log(response)
                    window.location.href = 'http://localhost:8000'+response;
                },
                error: function (response) {
                    console.log(response)
                }
            })

    })