<template>
  <div class="home">
    <vue-headful
      title="Calma - Diminua sua ansiedade durante o COVID-19"
      description="Converse e desabafe com um voluntário treinado para diminiur a sua ansiedade nestes tempos de COVID-19"
    />
    <section class="section">
      <div class="container">
	<img width="220" src="../assets/friendly_face.svg" />
	<br>
	<h1 class="title">Muita calma nesta hora.</h1>
	<h2 class="subtitle">Converse e desabafe nestes tempos de COVID-19.</h2>
	<br>
	<a class="button is-large is-rounded is-info" href="javascript:void(Tawk_API.toggle())">Conversar com voluntário</a> 
      </div>
    </section>
    <section>
      <div class="container">
	<div class="columns">
	  <div class="column">
	    <img width="150" src="../assets/woman-student.svg" />
	    <h2 class="title">Voluntários de Excelência</h2>
	    <p class="is-size-5">Converse com estudantes de doutorado, mestrado e graduação das melhores instituições de ensino do Brasil e Argentina. <router-link to="/about">Conheça nossa equipe</router-link>.</p>
	  </div>
	  <div class="column">
	    <img width="150" src="../assets/woman-teacher.svg" />
	    <h2 class="title">Supervisores de Excelência</h2>
	    <p class="is-size-5">Equipe de supervisores possui anos de experiência em diversas áreas ligadas à saúde mental e física. <router-link to="/about">Conheça nossa equipe</router-link>.</p>
	  </div>
	  <div class="column">
	    <img width="150" src="../assets/colaboration.svg" />
	    <h2 class="title">Suporte Gratuito e de Qualidade</h2>
	    <p class="is-size-5">Neste momento difícil do COVID-19, nos juntamos para ajudar você.</p>
	  </div>
	</div>
      </div>
    </section>
    <Footer />
  </div>
</template>

<script>
import Footer from '@/components/footer.vue';

export default {
  name: "Home",
  components: {
    Footer
  }
};
</script>

<style scoped>
.home {
  text-align: center;
}

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
