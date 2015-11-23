/*
 *  Document   : tablesDatatables.js
 *  Author     : pixelcave
 *  Description: Custom javascript code used in Tables Datatables page
 */

var TablesDatatables = function() {
    console.log("this datatables file works.");
    return {
        init: function() {
            /* Initialize Bootstrap Datatables Integration */
            App.datatables();
            /* Initialize Datatables */
            // $('#example-datatable').dataTable({
            //     "aoColumnDefs": [ { "bSortable": false, "aTargets": [ 1, 4 ] } ],
            //     "iDisplayLength": 10,
            //     "aLengthMenu": [[10, 20, 30, -1], [10, 20, 30, "All"]]
            // });
            // $('#example-datatable').dataTable({
            //     "aoColumnDefs": [ { "bSortable": false, "aTargets": [ 1, 2 ] } ],

            // });
            console.log("this datatables file works.222");
            $('#example-datatable').DataTable(
                {"iDisplayLength": 10,
                }
            );
            //table.order( [ 1, 'desc' ] ).draw();

            /* Add placeholder attribute to the search input */
            $('.dataTables_filter input').attr('placeholder', 'Search');

        }
    };
}();