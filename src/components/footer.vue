<template>
  <div>
    <footer class="footer"> 
      <div class="container">
	<div class="columns">
	  <div class="column is-one-fourth">
	    <h1 class="title">{{ $t("footer_calma") }}</h1>
	  </div>
	  <div class="column">
	    <h1 class="title">{{ $t("footer_realizacao") }}</h1>
	    <div class="columns">
	      <!-- Start column -->
	      <div class="column">
		<figure class="image is-128x128">
		  <img src="../assets/ufv.png">
		</figure>
	      </div>
	      <!-- End column -->
	      <!-- Start column -->
	      <div class="column">
		<figure class="image is-128x128">
		  <img src="../assets/ufjf.png">
		</figure>
	      </div>
	      <!-- End column -->
	      <!-- Start column -->
	      <div class="column">
		<figure class="image is-128x128">
		  <img src="../assets/ucp.png">
		</figure>
	      </div>
	      <!-- End column -->
	      <div class="column">
		<figure class="image is-128x128">
		  <img src="../assets/unt.png">
		</figure>
	      </div>
	      <!-- End column -->
	      <!-- Start column -->
	      <div class="column">
		<figure class="image is-128x128">
		  <img src="../assets/universo.png">
		</figure>
	      </div>
	      <!-- End column -->
	    </div>
	  </div>
	</div>
      </div>
     <div class="container">
       <p>{{ $t("footer_description") }}.</p>
       <p>{{ $t("footer_project_github") }}<a href="https://github.com/henriquepgomide/calma-webapp">Github</a>.</p>
     </div> 
    </footer> 
  </div>
</template>
<style scoped>
.footer {
  margin-top: 10rem;
}

h1, p {
  text-align: left;
}
</style>
