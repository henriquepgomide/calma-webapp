<template>
  <div class="home">
    <vue-headful
      :title="$t('main_title_seo')"
      :description="$t('main_description_seo')"
      />
      <section class="section">
	<div class="container">
	  <img width="220" src="../assets/friendly_face.svg" />
	  <br>
	  <h1 class="title">{{ $t("main_title") }}</h1>
	  <h2 class="subtitle">{{ $t("main_subtitle") }}</h2>
	  <br>
	  <a class="button is-large is-rounded is-info" href="javascript:void(Tawk_API.toggle())">{{ $t("main_button_text") }}</a> 
	</div>
      </section>
      <section>
	<div class="container">
	  <div class="columns">
	    <div class="column">
	      <img width="150" src="../assets/woman-student.svg" />
	      <h2 class="title">{{ $t("main_col1_header") }}</h2>
	      <p class="is-size-5">{{ $t("main_col1_text") }} <router-link to="/about">{{ $t("main_col_text_h") }}<router-link to="/about"></router-link></router-link>.</p>
	    </div>
	    <div class="column">
	      <img width="150" src="../assets/woman-teacher.svg" />
	      <h2 class="title">{{ $t("main_col2_header") }}</h2>
	      <p class="is-size-5">{{ $t("main_col2_text") }}<router-link to="/about">{{ $t("main_col_text_h") }}</router-link>.</p>
	    </div>
	    <div class="column">
	      <img width="150" src="../assets/colaboration.svg" />
	      <h2 class="title">{{ $t("main_col3_header") }}</h2>
	      <p class="is-size-5">{{ $t("main_col3_text") }}</p>
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
