$(document).ready(function() {
	var reset_game = function() {
		$("#red-car").animate({left: "0"}, 10);
		$("#green-car").animate({left: "0"}, 10);
		$("#cscore").text(0);	
		$("#pscore").text(0);	
	};

	var take_turn = function(e) {
		$.getJSON("take-turn", {'action': e.which}, function(resp) {
			$("#cscore").text(resp.computer_score);	
			$("#pscore").text(resp.player_score);	
			if (resp.won) {
				$("#red-car").animate({left: "+=10"}, 10);
			} else {
				$("#green-car").animate({left: "+=10"}, 10);
			}
			if (resp.computer_score == 50 || resp.player_score == 50) {
				reset_game();
				$.post('game-over');
			}
		});
	};

	$(document).keydown(function(e) {
		if (e.which == 37 || e.which == 39) {
			take_turn(e);
		} else if (e.which == 82) {
			reset_game();
			$.post('game-over');
		}
	});	
});
