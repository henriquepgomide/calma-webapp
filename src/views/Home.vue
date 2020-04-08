<template>
  <div class="home">
    <section class="section">
      <div class="container">
	<img width="220" src="../assets/friendly_face.svg" />
	<br>
	<h1 class="title">Muita calma nesta hora.</h1>
	<br>
	<a class="button is-large is-rounded is-success" href="javascript:void(Tawk_API.toggle())">Conversar com alguém</a> 
      </div>
    </section>

    <section>
      <div class="container">
	<div class="columns">
	  <div class="column">
	    <img width="150" src="../assets/woman-student.svg" />
	    <h2 class="title">Voluntários de Excelência</h2>
	    <p class="is-size-5">Converse com estudantes de doutorado, mestrado e graduação das melhores instituições de ensino do Brasil e Argentina.<a href="#">Veja nossa equipe</a>.</p>
	  </div>
	  <div class="column">
	    <img width="150" src="../assets/woman-teacher.svg" />
	    <h2 class="title">Supervisores de Excelência</h2>
	    <p class="is-size-5">Equipe de supervisores possui anos de experiência em diversas áreas ligadas à saúde mental e física. <a href="#">Veja nossa equipe</a>.</p>
	  </div>
	  <div class="column">
	    <img width="150" src="../assets/colaboration.svg" />
	    <h2 class="title">Suporte Gratuito e de Qualidade</h2>
	    <p class="is-size-5">Neste momento difícil do COVID-19, nos juntamos para ajudar você.</p>
	  </div>
	</div>
      </div>
    </section>

<!--    <section>
      <div class="container">
	<div class="columns">
	<div class="column">UFV</div>
	<div class="column">UFJF</div>
	<div class="column">UNIVERSO</div>
	<div class="column">UNIVERSIDAD NACIONAL DE TUCUMAN</div>
	<div class="column">UNIVERSIDADE CATÓLICA DE PETROPÓLIS</div>

	</div>
      </div>
</section> -->

  </div>
</template>

<script>
export default {
  name: "Home",
  components: {
  }
};
</script>

<style scoped>
h1 {
  font-family: 'Gotu', sans-serif;
}

h2 {
  font-family: 'Muli', sans-serif;
  font-weight: 'bold';
}

p {
  text-align: center;
}
</style>
