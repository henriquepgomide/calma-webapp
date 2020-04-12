<template>
  <div>
    <b-navbar>
        <template slot="brand">
            <b-navbar-item tag="router-link" :to="{ path: '/' }">
                <img
                    src="../assets/friendly_face.png"
                    alt="Lightweight UI components for Vue.js based on Bulma"
                >
            </b-navbar-item>
        </template>
        <template slot="start">
	  <b-navbar-item tag="router-link" :to="{ path: '/' }">
                Principal
            </b-navbar-item>
	    <b-navbar-item tag="router-link" :to="{ path: '/about' }">
                Equipe
            </b-navbar-item>
        </template>
        <template slot="end">
	  <b-navbar-item tag="div">
	    <div class="buttons">
	      <a class="button is-rounded is-info" href="javascript:void(Tawk_API.toggle())">Conversar</a> 
	    </div>
	  </b-navbar-item>
        </template>
    </b-navbar>
  </div>
</template>
<style scoped>
nav {
  font-size: 1.3rem;
}
</style>
