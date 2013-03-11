$(document).ready(function(){
    // DataTables para busca por clientes
    $('#table-clients').dataTable({
        "sScrollY": "200px",
        "bPaginate": false,
        "bScrollCollapse": true,
        "bJQueryUI": true,
    });

    // Mascaras nos campos dos formularios
    //$('#id_cpf').mask("999.999.999-99"); // Estudar como aplicar a mascara somente para exibicao e enviar somente a string sem pontos e traco
    $('#id_birthday').mask("99/99/9999");
    //$('#id_phone').mask("(999) 9999-9999"); // Mesmo de cima
});