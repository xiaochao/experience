var is_load = false;

function MyLoad(load_id, load_page){
            var ajaxobj = new AJAXRequest;
            ajaxobj.method = "GET";
            ajaxobj.url = load_page;
            ajaxobj.callback = function(xmlobj) {
                if (!is_load){
                    document.getElementById(load_id).innerHTML += xmlobj.responseText;
                    is_load = true;
                }else{
                    document.getElementById(load_id).innerHTML = "";
                    is_load = false;
                }
            }
            ajaxobj.send();
        }


function MySubmit(){
    var $sbt_value=$("#id_vomit").val();
    var $url="http://127.0.0.1:8000/comment";
    $.post($url,
            {'vomit':$sbt_value},
            function(data){
            }
    )
}