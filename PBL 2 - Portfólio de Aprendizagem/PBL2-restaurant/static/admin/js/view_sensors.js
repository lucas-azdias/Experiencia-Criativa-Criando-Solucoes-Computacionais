$(document).ready(function () {
    var table = $('#view_sensors').DataTable( {
        scrollY:        "500px",
        scrollX:        true,
        scrollCollapse: true,
        paging:         true,
        fixedColumns:   {
            heightMatch: 'none'
        },
        language: {
            url:"static/language/pt_br.json"
        }
    } );
});