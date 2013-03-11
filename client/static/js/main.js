$(document).ready(function(){
    var cont = 0;

    // DataTables para busca por clientes
    $('#table-clients').dataTable({
        "sScrollY": "200px",
        "bPaginate": false,
        "bScrollCollapse": true,
        "bJQueryUI": true,
    }).columnFilter({
            aoColumns: [
                null,
                {sSelector: '#sex_filter', type: 'select'},
                null,
                null,
                null,
                null,
                null,
                {sSelector: '#dist_filter', type: 'text'},
                {sSelector: '#zone_filter', type: 'text'},
                {sSelector: '#city_filter', type: 'text'}
            ]
        });

    // Mascaras nos campos dos formularios
    //$('#id_cpf').mask("999.999.999-99"); // Estudar como aplicar a mascara somente para exibicao e enviar somente a string sem pontos e traco
    $('#id_birthday').mask("99/99/9999");
    //$('#id_phone').mask("(999) 9999-9999"); // Mesmo de cima

    // Esconder e mostrar campos extras de telefone
    $('#add_phone').click(function(){
        if(cont == 0) {
            $('#phone1').removeClass('no_display');
            cont++;
        } else if(cont==1) {
            $('#phone2').removeClass('no_display');
            cont++;
        } else {
            alert("Maximo de 3 telefones")
        }
    });
});