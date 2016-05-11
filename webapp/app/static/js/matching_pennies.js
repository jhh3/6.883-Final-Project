$(document).ready(function() {
	var game_number = 0;
	var reset_game = function() {
		$("#red-car").animate({left: "0"}, 10);
		$("#green-car").animate({left: "0"}, 10);
		$("#cscore").text(0);	
		$("#pscore").text(0);	
	};

	var add_to_history = function(cs, ps, won) {
		var bot_choice = $('input[name=bot-choice]:checked', '#radio-bot').val(); 
		var new_history = "<tr>";
		new_history += "<td>" + game_number + "</td>";
		new_history += "<td>" + bot_choice + "</td>";
		new_history += "<td>" + ps + "</td>";
		new_history += "<td>" + cs + "</td>";
		if (!won) {
			new_history += "<td>Won</td>";
		} else {
			new_history += "<td>Lost</td>";
		}
		new_history += "</tr>";
		game_number += 1;
		$("#history-table tbody").prepend(new_history);
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
				add_to_history(resp.computer_score, resp.player_score, resp.won)
				reset_game();
				$.post('game-over');
			}
		});
	};

	var change_bot = function(bot) {
		$.post('change-bot', {'bot': bot}, function() {
			reset_game();
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

	$('#radio-bot input').on('change', function() {
		var bot_choice = $('input[name=bot-choice]:checked', '#radio-bot').val(); 
		change_bot(bot_choice);
		$("#radio-bot input").blur();
	});

	// Start off with Shannon
	change_bot('Shannon');
});
