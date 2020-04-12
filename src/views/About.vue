<template>
  <div class="about">
    <vue-headful
      title="Calma | Conheça a equipe e o projeto"
      description="Conheça a equipe de especialistas e voluntários que mantém este projeto"
    />

      <section class="section">
	<div class="container">
	  <h1 class="title">Equipe</h1>
	  <p class="is-size-5">Conheça a equipe de supervisores e voluntários do projeto.</p>
	</div>
      </section>
        <section class="section">
      <div class="container">
	<div v-for="people in team" :key="people.name">
	  <PersonCard
	    :name=people.name
	    :photo_link=people.photo_link
	    :description=people.description
	    :link=people.link
	  />
	  <br>
	  <br>
	  <br>
	</div>
      </div>
    </section>
  </div>
</template>
<script>
import PersonCard from "@/components/personcard.vue";
import team from "../assets/team/team.json";

export default {
  components: {
    PersonCard
  },
  data() {
    return {
      team
    }
  }
}
</script>
