$(document).ready(function() {
	$(document).keydown(function(e) {
		if (e.which == 37) {
			$("#last-action").text("Entered: 0");
		} else if (e.which == 39) {
			$("#last-action").text("Entered: 1");
		}

		$.getJSON("take-turn", {'action': e.which}, function(resp) {
			$("#cscore").text("Computer score: " + resp.computer_score);	
			$("#pscore").text("Player score: " + resp.player_score);	
			if (resp.won) {
				$("#red-car").animate({left: "+=10"}, 10);
			} else {
				$("#green-car").animate({left: "+=10"}, 10);
			}
			if (resp.computer_score == 50 || resp.player_score == 50) {
				$("#red-car").animate({left: "0"}, 10);
				$("#green-car").animate({left: "0"}, 10);
				$("#cscore").text("Computer score: ");	
				$("#pscore").text("Player score: ");	
				$.post('game-over');
			}
		});
	});	
});
