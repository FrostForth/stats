<script type="text/javascript">

	var height = window.innerHeight
	|| document.documentElement.clientHeight
	|| document.body.clientHeight;

	window.onload = grabImages();

  function grabImages() {
   fetch("https://api.github.com/repos/frostforth/stats/contents/Gallery?ref=gh-pages")
   .then(data => data.json())
   .then(data => {
      var mainContainer = document.getElementById("myData");
      for (var i = 0; i < data.length; i++) {
      var img = document.createElement("img");
      
      img.height = height;
      img.alt = data[i].name;
      img.src = data[i].download_url;
      mainContainer.appendChild(img);
    	}
   });
  }
</script>

<p id="myData">
</p>
