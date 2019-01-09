let boxer_1 = {
  name: "Tyson",
  hits: 0,
  knockdowns: 0,
  penalties: 0
}

let boxer_2 = {
  name: "Nathan",
  hits: 0,
  knockdowns: 0,
  penalties: 0
}

const boxer_1_glove = document.getElementById('boxer_1_glove');
const boxer_2_glove = document.getElementById('boxer_2_glove');
const boxer_1_knockdown = document.getElementById('boxer_1_knockdown');
const boxer_2_knockdown = document.getElementById('boxer_2_knockdown');
const boxer_1_penalty = document.getElementById('boxer_1_penalty');
const boxer_2_penalty = document.getElementById('boxer_2_penalty');
const next_round = document.getElementById('next_round');


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

  next_round.addEventListener('click', function() {
    print_scores();
  })

}

main();
