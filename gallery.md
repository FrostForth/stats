<script type="text/javascript">

	window.onload = grabImages();

  function grabImages() {
   fetch("https://api.github.com/repos/frostforth/stats/contents/Gallery?ref=gh-pages")
   .then(data => data.json())
   .then(data => {
      Var maincontainer = document.getElementById("main");
      for (var i = 0; i < data.length; i++) {
      var img = document.createElement("img");
      img.alt = data[i].name;
      img.src = data[i].download_url;
      mainContainer.appendChild(img);
      alert(data[i].name);
    	}
   });
  }
</script>

<p id="main">
</p>
