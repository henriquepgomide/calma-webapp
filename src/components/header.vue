<template>
  <div>
    <b-navbar>
      <template slot="brand">
        <b-navbar-item tag="router-link" :to="{ path: '/' }">
          <img src="../assets/friendly_face.png" alt="Logo do Calma" />
        </b-navbar-item>
      </template>
      <template slot="start">
        <b-navbar-item tag="router-link" :to="{ path: '/' }">
          {{ $t("navbar_principal") }}
        </b-navbar-item>
        <b-navbar-item tag="router-link" :to="{ path: '/about' }">
          {{ $t("navbar_equipe") }}
        </b-navbar-item>
        <b-navbar-item tag="router-link" :to="{ path: '/services' }">
          {{ $t("navbar_onde_buscar_ajuda") }}
        </b-navbar-item>
        <b-navbar-item tag="router-link" :to="{ path: '/libraries' }">
          {{ $t("navbar_libraries") }}
        </b-navbar-item>
      </template>

      <template slot="end">
        <b-navbar-dropdown label="Idioma">
          <b-navbar-item @click="changeLocale('es')">
            🇦🇷 - Español
          </b-navbar-item>
          <b-navbar-item @click="changeLocale('pt')">
            🇧🇷 - Português do Brasil
          </b-navbar-item>
        </b-navbar-dropdown>
        <b-navbar-item tag="div">
          <div class="buttons">
            <a
              class="button is-rounded is-info"
              href="javascript:void(Tawk_API.toggle())"
            >
              {{ $t("navbar_conversar") }}</a
            >
          </div>
        </b-navbar-item>
      </template>
    </b-navbar>
  </div>
</template>
<script>
export default {
  methods: {
    changeLocale: function(locale) {
      this.$i18n.locale = locale;
    }
  }
};
</script>
<style scoped>
nav {
  font-size: 1.3rem;
}
</style>
