const boxer_1_glove = document.getElementById('boxer_1_glove');
const boxer_2_glove = document.getElementById('boxer_2_glove');
const boxer_1_knockdown = document.getElementById('boxer_1_knockdown');
const boxer_2_knockdown = document.getElementById('boxer_2_knockdown');
const boxer_1_penalty = document.getElementById('boxer_1_penalty');
const boxer_2_penalty = document.getElementById('boxer_2_penalty');
const next_round = document.getElementById('next_round');
var boxer_1_name = document.getElementById('boxer_1_name').innerHTML;
var boxer_2_name = document.getElementById('boxer_2_name').innerHTML;
var game_id_js = document.getElementById('game_id_js').innerHTML;

let boxer_1 = {
  name: boxer_1_name,
  hits: 0,
  knockdowns: 0,
  penalties: 0
}

let boxer_2 = {
  name: boxer_1_name,
  hits: 0,
  knockdowns: 0,
  penalties: 0
}

function increment(boxer, score_type) {
  switch (score_type) {
    case "hits":
      boxer.hits++;
      console.log(boxer.hits);
      break;
    case "knockdowns":
      boxer.knockdowns++;
      console.log(boxer.knockdowns);
      break;
    case "penalties":
      boxer.penalties++;
      console.log(boxer.penalties);
      break;
    }
}

function print_scores() {
  console.log("Boxer 1: " + JSON.stringify(boxer_1));
  console.log("Boxer 2: " + JSON.stringify(boxer_2));
}

function main() {
  boxer_1_glove.addEventListener('click', function() {
    increment(boxer_1, "hits");
  })

  boxer_2_glove.addEventListener('click', function() {
    increment(boxer_2, "hits");
  })

  boxer_1_knockdown.addEventListener('click', function() {
    increment(boxer_1, "knockdowns");
  })

  boxer_2_knockdown.addEventListener('click', function() {
    increment(boxer_2, "knockdowns");
  })

  boxer_1_penalty.addEventListener('click', function() {
    increment(boxer_1, "penalties");
  })

  boxer_2_penalty.addEventListener('click', function() {
    increment(boxer_2, "penalties");
  })

  if (localStorage.getItem('round_number') === null) {
    var fight_id_js = document.getElementById('fight_id_js').innerHTML;
    localStorage.setItem('fight_id_js', fight_id_js);
    var round_number = 1;
  }
  else {
    var fight_id_js = localStorage.getItem('fight_id_js');
    var round_number = localStorage.getItem('round_number');
  }
  document.getElementById('round_number_span').innerHTML = round_number;

  if (round_number == 12) {
    document.getElementById("next_round").innerHTML = "See your Scores";
  }


  next_round.addEventListener('click', function() {
    document.getElementById("id_game_id").getElementsByTagName('option')[game_id_js].selected = 'selected';
    document.getElementById("id_round_number").setAttribute("value", round_number);
    document.getElementById("id_boxer_1_hits").setAttribute("value", boxer_1.hits);
    document.getElementById("id_boxer_1_knockdowns").setAttribute("value", boxer_1.knockdowns);
    document.getElementById("id_boxer_1_penalties").setAttribute("value", boxer_1.penalties);
    document.getElementById("id_boxer_2_hits").setAttribute("value", boxer_2.hits);
    document.getElementById("id_boxer_2_knockdowns").setAttribute("value", boxer_2.knockdowns);
    document.getElementById("id_boxer_2_penalties").setAttribute("value", boxer_2.penalties);

    boxer_1.hits = 0;
    boxer_1.knockdowns = 0;
    boxer_1.penalties = 0;

    boxer_2.hits = 0;
    boxer_2.knockdowns = 0;
    boxer_2.penalties = 0;

    document.getElementById("game_form").submit();

    round_number++;
    localStorage.setItem('round_number', round_number);


   })

   if (round_number == 13) {
     localStorage.clear();
     window.open('/games/game-' + game_id_js + '/', '_self');
   }

}

main();
