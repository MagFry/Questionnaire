// https://bootsnipp.com/snippets/dlaaN
function add_star(ths,sno,movie_id){
  for (var i=1;i<=6;i++){
    var cur=document.getElementById("star"+i+"-"+movie_id)
    cur.className="fa fa-star"
  }
  for (var i=1;i<=sno;i++){
    var cur=document.getElementById("star"+i+"-"+movie_id)
    if(cur.className=="fa fa-star")
    {
      // mark stars as checked and notseen as not checked
      cur.className="fa fa-star checked"
      document.getElementById("notseen-"+movie_id).className="fa fa-close"
    }
  }
}
function add_notseen(ths,movie_id){
  var cur=document.getElementById("notseen-"+movie_id)
  if(cur.className=="fa fa-close")
  {
    // mark stars as not checked and notseen as checked
    cur.className="fa fa-close checked"
    document.getElementById("star"+1+"-"+movie_id).className="fa fa-star"
    document.getElementById("star"+2+"-"+movie_id).className="fa fa-star"
    document.getElementById("star"+3+"-"+movie_id).className="fa fa-star"
    document.getElementById("star"+4+"-"+movie_id).className="fa fa-star"
    document.getElementById("star"+5+"-"+movie_id).className="fa fa-star"
    document.getElementById("star"+6+"-"+movie_id).className="fa fa-star"
  }
}
// parses current document and gets an array of
// currently rendered movies ids
// (returns array of integers)
function get_movie_ids(ths) {
  var movie_notseen_elements = $('*[id^="notseen-"]');
  var movie_ids = new Array();
  for (var i=0; i<movie_notseen_elements.length; i++) {
    // e.g. notseen-25
    var css_identifier = movie_notseen_elements[i].id
    var movie_id = css_identifier.split('-')[1]
    movie_ids.push(movie_id)
  }
  return movie_ids
}
// parses current document and gets an array of
// dictionaries of movie_id + rating
function get_movies_ratings(ths, movie_ids, alert_each_rating) {
  var ratings = new Array();
  for (var i=0; i<movie_ids.length; i++) {
    // for each movie
    movie_id = movie_ids[i]
    rating = 0
    if (document.getElementById("notseen-"+movie_id).className.includes("checked")) {
      rating = -1
    } else if (document.getElementById("star"+6+"-"+movie_id).className.includes("checked")) {
      rating = 6
    } else if (document.getElementById("star"+5+"-"+movie_id).className.includes("checked")) {
      rating = 5
    } else if (document.getElementById("star"+4+"-"+movie_id).className.includes("checked")) {
      rating = 4
    } else if (document.getElementById("star"+3+"-"+movie_id).className.includes("checked")) {
      rating = 3
    } else if (document.getElementById("star"+2+"-"+movie_id).className.includes("checked")) {
      rating = 2
    } else if (document.getElementById("star"+1+"-"+movie_id).className.includes("checked")) {
      rating = 1
    }
    ratings.push({
      movie_id: movie_id,
      movie_rating: rating
    })
    if (alert_each_rating == true) {
      alert('movie id: ' + movie_id + ' rating: '+ rating);
    }
  }
  return ratings
}
function check_all_movies_rated(ths, ratings){
  for (var i=0; i<ratings.length; i++) {
    if (ratings[i].movie_rating == 0) {
      return false
    }
  }
  return true
}
// used in test view only, does not send any data
function print_rate(ths){
  movie_ids = get_movie_ids()
  ratings = get_movies_ratings(ths, movie_ids, true)
  all_movies_rated = check_all_movies_rated(ths,ratings)
  if (all_movies_rated == false) {
    alert("Not all movies are rated")
  }
}
// used in production view, sends data with POST method
function save_ratings(ths){
  movie_ids = get_movie_ids()
  ratings = get_movies_ratings(ths, movie_ids, false)
  all_movies_rated = check_all_movies_rated(ths,ratings)
  if (all_movies_rated == false) {
    alert("Not all movies are rated")
    // this and onclick="return save_ratings()" prevents the page
    // from being refreshed and pointing to next movies category
    return false
  }
  my_post_data = {
    ratings: ratings
  }
  my_post_data_str = JSON.stringify(my_post_data)
  $.ajax({
    type: "POST",
    url: "/movies/insert_rating/",
    data: my_post_data_str,
    // make it visible on your web browser developer tools
    success: console.log(my_post_data_str),
    dataType: 'JSON'
  });
}
