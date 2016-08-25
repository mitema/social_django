$(function(){

	$('#user').blur(function(){
		$.ajax({
			type: 'POST',
			url: '/social/checkuser/',
			data : {
				'user' : $('#user').val(),
				'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()
			},
			success: checkuseranswer,
			dataType: 'html'
		});
	});

});

function checkuseranswer(data, textStatus, jqHXR)
{
	$('#info').html(data);
}