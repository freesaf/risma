$.fn.serializeObject = function()
{
    var o = {};
    var a = this.serializeArray();
    $.each(a, function() {
        if (o[this.name] !== undefined) {
            if (!o[this.name].push) {
                o[this.name] = [o[this.name]];
            }
            o[this.name].push(this.value || '');
        } else {
            o[this.name] = this.value || '';
        }
    });
    return o;
};

function isInteger(value) {
    if ((undefined === value) || (null === value)) {
        return false;
    }
    return value % 1 == 0;
}
var wbc_cart = {
	config : {},
	do_ajax : function(url, dataToSend, success_function) {
		$.ajax({
			  url: this.config[url+'_url'],
			  type : "POST",
			  data : dataToSend,
			  success: success_function,
			  error: function(xhr, ajaxOptions, thrownError){
				  //alert(xhr.status + ' : ' + thrownError);
			  }
			});
	},
	//Ajout de produit
	add : function (form){
		var form_data = $("#" + form).serializeObject();
		var overlay = $("#" + form).parent().parent().parent().parent();
		if(form_data.variant == '_'){
			//$('.error_select').show();	
			showpopup(overlay);
			return false;			
		}
		
		var quantite = form_data.quantite;
		if (quantite < 1 || !isInteger(quantite)){
			//alert("La quantité doit être un nombre entier supérieur à 0");
			throw new Error();
		}
		if(form_data.variant != '_' || quantite > 1 || isInteger(quantite)) {
			closePopup(overlay);
		}
		success_function = function(res){
			$('#form_panier').html(res);
		};
		this.do_ajax('add', form_data, success_function);
		//Close();
	},
	//Suppresion d'un produit
	del : function (key, src, template){
		var data = "key=" +key+ "&csrfmiddlewaretoken=" + $('input[name=csrfmiddlewaretoken]').val() + "&src=" + src + "&template=" + template;
		success_function = function(res){
			$('#'+key).hide(300, function () {
				//console.log(res);
			});
			$('#form_panier').html(res);
		};
		this.do_ajax('del', data, success_function);
		return false;
	},
	//MAJ de la quantité d'un produit
	update_quantity : function(key, value, src, template){
		if (value < 1 || !isInteger(value)){
			alert("La quantité doit être un nombre entier supérieur à 0");
			throw new Error();
		}
		var data = "key=" +key+ "&quantity=" +value+ "&csrfmiddlewaretoken=" + $('input[name=csrfmiddlewaretoken]').val() + "&src=" + src + "&template=" + template;
		success_function = function(res){
			$('#form_panier').html(res);	
		};
		this.do_ajax('update_quantity', data, success_function);

	}
};
