<template>
  <div class="team">
    <vue-headful
      :title="$t('team_page_title_seo')"
      :description="$t('team_page_description_seo')"
    />
    <section class="section">
      <div class="container">
        <h1 class="title is-size-1">{{ $t("team_page_header") }}</h1>
        <p class="is-size-5">{{ $t("team_page_description") }}</p>
      </div>
    </section>
    <section class="section">
      <div class="container">
        <h2 class="subtitle is-size-1">Pesquisadores e Supervisores</h2>
        <br />
        <div v-for="people in team.slice(0, 10)" :key="people.name">
          <PersonCard
            :name="people.name"
            :photo_link="people.photo_link"
            :description="people.description"
            :link="people.link"
          />
          <br />
          <br />
          <br />
        </div>
      </div>

      <div class="container">
        <h2 class="subtitle is-size-1">Voluntários</h2>
        <br />
        <div v-for="people in team.slice(10)" :key="people.name">
          <PersonCard
            :name="people.name"
            :photo_link="people.photo_link"
            :description="people.description"
            :link="people.link"
          />
          <br />
          <br />
          <br />
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
    };
  }
};
</script>
